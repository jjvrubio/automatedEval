from __future__ import annotations

import tempfile
import unittest
import hashlib
from pathlib import Path

from stage1.csv_input import InputRow
from stage1.storage import Stage1Store
from stage2.runner import eligible_rows, run_stage2
from stage2.deliverables import resolve_deliverables_root


def criterion(value: int) -> dict:
    return {
        "canonical_company_name": "Example",
        "identity_status": "matched",
        "value_type": "exact",
        "value": value,
        "lower_bound": None,
        "upper_bound": None,
        "evidence": [{"url": "https://example.com/source"}],
    }


def theme(name: str, category: str) -> dict:
    source = {
        "title": "Official source",
        "url": f"https://example.com/{name}",
        "publisher": "Example",
        "published_date": "2026-01-01",
        "source_type": "official",
        "scope": "company",
        "excerpt": "Supported finding.",
    }
    return {
        "theme": name,
        "executive_summary": f"Summary for {name}.",
        "current_state": f"Current state for {name}.",
        "findings": [
            {
                "category": category,
                "title": f"Finding {name}",
                "date": "2026-01-01",
                "status": "confirmed",
                "finding": "Supported finding.",
                "business_relevance": "Relevant for discovery.",
                "evidence": [source],
            }
        ],
        "opportunity_signals": [
            {
                "title": f"Signal {name}",
                "strength": "high",
                "rationale": "Grounded rationale.",
                "evidence_urls": [source["url"]],
            }
        ],
        "risks": ["Validate internal ownership."],
        "stakeholders": [],
        "potentiality_score": 8,
        "score_rationale": "Strong public signal.",
        "recommended_discovery_questions": [f"Question about {name}?"],
        "evidence_quality": "high",
        "missing_information": ["Internal architecture is not public."],
    }


class FakeStage2Researcher:
    def __init__(self) -> None:
        self.calls = 0

    def research_technology(self, *_):
        self.calls += 1
        return theme("technology", "crm"), {"kind": "technology"}

    def research_corporate(self, *_):
        self.calls += 1
        return theme("corporate", "leadership_change"), {"kind": "corporate"}

    def research_expansion(self, *_):
        self.calls += 1
        return theme("expansion", "market_entry"), {"kind": "expansion"}

class FakeExcludedResearcher(FakeStage2Researcher):
    def research_technology(self, *_):
        self.calls += 1
        result = theme("technology", "crm")
        result.update(
            {
                "sector_profile": "excluded_banking",
                "sector_eligibility": "excluded",
                "sector_rationale": "Banking is out of scope.",
            }
        )
        return result, {"kind": "technology"}


class Stage2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.row = InputRow(
            record_id="eligible-record",
            source_row=2,
            values={
                "Company Name": "Example",
                "# Employees": "150",
                "Website": "https://example.com",
                "Company Linkedin Url": "https://linkedin.com/company/example",
                "Number of Retail Locations": "12",
            },
        )

    def _create_eligible_stage1(self, output: Path) -> None:
        with Stage1Store(output / "stage1_state.sqlite3") as store:
            store.mark_running(self.row)
            store.save_success(
                self.row,
                criterion(150),
                criterion(12),
                {
                    "employees_decision": "VERIFIED_PASS",
                    "locations_decision": "VERIFIED_PASS",
                    "stage1a_decision": "PASS_1A",
                },
                [],
            )
            store.save_revenue_success(
                self.row,
                criterion(20_000_000),
                {
                    "revenue_decision": "VERIFIED_PASS",
                    "eligibility_decision": "ELIGIBLE",
                },
                {},
            )

    def test_only_eligible_rows_enter_stage2(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            self._create_eligible_stage1(output)
            selected = eligible_rows([self.row], output)
            self.assertEqual(len(selected), 1)
            self.assertEqual(selected[0][0].company_name, "Example")

    def test_default_deliverables_root_is_csv_parent(self) -> None:
        csv_path = Path("/tmp/imports/companies.csv")
        self.assertEqual(
            resolve_deliverables_root(csv_path),
            Path("/tmp/imports").resolve(),
        )
        self.assertEqual(
            resolve_deliverables_root(csv_path, Path("/tmp/accounts")),
            Path("/tmp/accounts").resolve(),
        )

    def test_runner_generates_report_and_resumes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            self._create_eligible_stage1(output)
            candidates = eligible_rows([self.row], output)
            researcher = FakeStage2Researcher()
            deliverables = output / "accounts"
            paths = run_stage2(
                candidates,
                output,
                researcher,
                deliverables_root=deliverables,
            )
            self.assertEqual(researcher.calls, 3)
            self.assertTrue(paths["report"].exists())
            self.assertEqual(
                paths["report"],
                deliverables
                / "Example"
                / "02 - Potencialidad"
                / "Informe de potencialidad.md",
            )
            self.assertTrue(
                (
                    deliverables
                    / "Example"
                    / "01 - Elegibilidad"
                    / "Resultado Etapa 1.md"
                ).exists()
            )
            self.assertTrue(
                (
                    deliverables
                    / "Example"
                    / "02 - Potencialidad"
                    / "Investigación"
                    / "Tecnología.json"
                ).exists()
            )
            report = paths["report"].read_text(encoding="utf-8")
            self.assertIn("PRIORIDAD_ALTA", report)
            self.assertIn("No se calculan ACV, ROI o payback", report)
            run_stage2(
                candidates,
                output,
                researcher,
                deliverables_root=deliverables,
            )
            self.assertEqual(researcher.calls, 3)

    def test_excluded_sector_stops_after_classification(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            self._create_eligible_stage1(output)
            candidates = eligible_rows([self.row], output)
            researcher = FakeExcludedResearcher()
            paths = run_stage2(candidates, output, researcher)
            self.assertEqual(researcher.calls, 1)
            self.assertNotIn("report", paths)

    def test_provided_meddicc_context_is_forwarded_to_researchers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            self._create_eligible_stage1(output)
            candidates = eligible_rows([self.row], output)

            class ContextCapturingResearcher(FakeStage2Researcher):
                def __init__(self) -> None:
                    super().__init__()
                    self.received_contexts: list[dict[str, object]] = []

                def research_technology(self, _, eligibility_context):
                    self.calls += 1
                    self.received_contexts.append(eligibility_context)
                    return theme("technology", "crm"), {"kind": "technology"}

            researcher = ContextCapturingResearcher()
            markdown = "# Example MEDDPICC"
            source = output / "Example - MEDDPICC.md"
            source.write_text(markdown, encoding="utf-8")
            run_stage2(
                candidates,
                output,
                researcher,
                provided_meddicc={
                    "source_path": str(source),
                    "sha256": "abc123",
                    "markdown": markdown,
                },
                use_provided_meddicc_as_context=True,
                deliverables_root=output / "accounts",
            )
            self.assertTrue(researcher.received_contexts)
            self.assertIn("provided_meddicc", researcher.received_contexts[0])
            self.assertEqual(
                researcher.received_contexts[0]["provided_meddicc"]["sha256"],
                "abc123",
            )

    def test_provided_meddpicc_has_priority_and_is_snapshotted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            self._create_eligible_stage1(output)
            candidates = eligible_rows([self.row], output)
            researcher = FakeStage2Researcher()
            markdown = (
                "---\nmeddpicc_stage: Active Discovery\n"
                "author: User\n---\n\n# Supplied MEDDPICC\n"
            )
            source = output / "Example - MEDDPICC.md"
            source.write_text(markdown, encoding="utf-8")
            paths = run_stage2(
                candidates,
                output,
                researcher,
                provided_meddicc={
                    "source_path": str(source),
                    "sha256": hashlib.sha256(
                        markdown.encode("utf-8")
                    ).hexdigest(),
                    "markdown": markdown,
                },
                deliverables_root=output / "accounts",
            )
            self.assertEqual(researcher.calls, 3)
            report = paths["report"].read_text(encoding="utf-8")
            self.assertIn("## MEDDPICC aportado", report)
            self.assertIn("Active Discovery", report)
            snapshots = list(
                (
                    output
                    / "accounts"
                    / "Example"
                    / "02 - Potencialidad"
                    / "Fuentes aportadas"
                ).glob("*.md")
            )
            self.assertEqual(len(snapshots), 1)
            self.assertIn(
                "Fuentes aportadas/Example - MEDDPICC.md",
                report,
            )

    def test_human_override_is_shown_as_effective_pass(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            self._create_eligible_stage1(output)
            candidates = eligible_rows([self.row], output)
            row, eligibility = candidates[0]
            eligibility["decision"].update(
                {
                    "employees_decision": "CONFLICTING",
                    "locations_decision": "CONFLICTING",
                }
            )
            eligibility["final_decision"].update(
                {
                    "stage1a_original_decision": "REVIEW_REQUIRED",
                    "stage1a_effective_decision": "PASS_1A",
                    "stage1a_override": True,
                }
            )
            paths = run_stage2(
                [(row, eligibility)],
                output,
                FakeStage2Researcher(),
                deliverables_root=output / "accounts",
            )
            eligibility_report = (
                output
                / "accounts"
                / "Example"
                / "01 - Elegibilidad"
                / "Resultado Etapa 1.md"
            ).read_text(encoding="utf-8")
            potentiality_report = paths["report"].read_text(encoding="utf-8")
            for report in (eligibility_report, potentiality_report):
                self.assertNotIn("| CONFLICTING |", report)
                self.assertIn("VERIFIED_PASS (revisión humana)", report)


if __name__ == "__main__":
    unittest.main()
