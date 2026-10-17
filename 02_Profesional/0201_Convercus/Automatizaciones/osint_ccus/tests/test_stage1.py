from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from stage1.csv_input import CsvValidationError, InputRow, read_csv
from stage1.policy import (
    CriterionDecision,
    StageDecision,
    evaluate_criterion,
    evaluate_final_eligibility,
    evaluate_stage1a,
)
from stage1.runner import run_stage1a, run_stage1b


def result(
    *,
    value_type: str = "exact",
    value: int | None = None,
    lower: int | None = None,
    upper: int | None = None,
    conflicting: bool = False,
    evidence: bool = True,
    threshold_consensus: str = "unknown",
) -> dict:
    return {
        "canonical_company_name": "Example",
        "identity_status": "matched",
        "identity_notes": "",
        "value_type": value_type,
        "value": value,
        "lower_bound": lower,
        "upper_bound": upper,
        "as_of_date": "2026-01-01",
        "scope": "company",
        "method": "published",
        "summary": "",
        "conflicting": conflicting,
        "confidence": "high",
        "threshold_consensus": threshold_consensus,
        "evidence": [{"url": "https://example.com"}] if evidence else [],
        "missing_information": [],
    }


class PolicyTests(unittest.TestCase):
    def test_strict_employee_boundary(self) -> None:
        self.assertEqual(
            evaluate_criterion(result(value=100), 100).decision,
            CriterionDecision.VERIFIED_FAIL,
        )
        self.assertEqual(
            evaluate_criterion(result(value=101), 100).decision,
            CriterionDecision.VERIFIED_PASS,
        )

    def test_strict_location_boundary(self) -> None:
        self.assertEqual(
            evaluate_criterion(result(value=10), 10).decision,
            CriterionDecision.VERIFIED_FAIL,
        )
        self.assertEqual(
            evaluate_criterion(result(value=11), 10).decision,
            CriterionDecision.VERIFIED_PASS,
        )

    def test_ranges_and_minimums(self) -> None:
        self.assertEqual(
            evaluate_criterion(
                result(value_type="range", lower=101, upper=200), 100
            ).decision,
            CriterionDecision.VERIFIED_PASS,
        )
        self.assertEqual(
            evaluate_criterion(
                result(value_type="range", lower=51, upper=200), 100
            ).decision,
            CriterionDecision.UNKNOWN,
        )
        self.assertEqual(
            evaluate_criterion(
                result(value_type="minimum", lower=11), 10
            ).decision,
            CriterionDecision.VERIFIED_PASS,
        )

    def test_conflict_and_missing_evidence(self) -> None:
        self.assertEqual(
            evaluate_criterion(result(value=200, conflicting=True), 100).decision,
            CriterionDecision.CONFLICTING,
        )
        self.assertEqual(
            evaluate_criterion(result(value=200, evidence=False), 100).decision,
            CriterionDecision.UNKNOWN,
        )

    def test_conflict_is_immaterial_when_all_sources_clear_threshold(self) -> None:
        self.assertEqual(
            evaluate_criterion(
                result(
                    value=509,
                    conflicting=True,
                    threshold_consensus="all_above",
                ),
                100,
            ).decision,
            CriterionDecision.VERIFIED_PASS,
        )

    def test_strict_revenue_boundary_and_final_gate(self) -> None:
        stage1a = evaluate_stage1a(
            evaluate_criterion(result(value=101), 100),
            evaluate_criterion(result(value=11), 10),
        )
        at_boundary = evaluate_criterion(result(value=15_000_000), 15_000_000)
        above_boundary = evaluate_criterion(result(value=15_000_001), 15_000_000)
        self.assertEqual(
            evaluate_final_eligibility(stage1a, at_boundary).decision,
            StageDecision.INELIGIBLE,
        )
        self.assertEqual(
            evaluate_final_eligibility(stage1a, above_boundary).decision,
            StageDecision.ELIGIBLE,
        )

    def test_combined_gate(self) -> None:
        passing = evaluate_criterion(result(value=101), 100)
        locations = evaluate_criterion(result(value=11), 10)
        self.assertEqual(
            evaluate_stage1a(passing, locations).decision,
            StageDecision.PASS_1A,
        )


class CsvTests(unittest.TestCase):
    def test_alias_and_extra_columns_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(
                    [
                        "company Name",
                        "# Employees",
                        "Website",
                        "Company Linkedin Url",
                        "Number of Retail Locations",
                        "Extra",
                    ]
                )
                writer.writerow(
                    [
                        "Example",
                        "120",
                        "https://example.com",
                        "https://linkedin.com/company/example",
                        "",
                        "keep",
                    ]
                )
            headers, rows = read_csv(path)
            self.assertEqual(headers[0], "Company Name")
            self.assertEqual(rows[0].values["Extra"], "keep")

    def test_missing_columns_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.csv"
            path.write_text("Company Name\nExample\n", encoding="utf-8")
            with self.assertRaises(CsvValidationError):
                read_csv(path)

    def test_duplicate_extra_columns_are_renamed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(
                    [
                        "Company Name",
                        "# Employees",
                        "Website",
                        "Company Linkedin Url",
                        "Number of Retail Locations",
                        "Industry",
                        "Industry",
                    ]
                )
                writer.writerow(["Example", "120", "", "", "", "Retail", "Fashion"])
            headers, rows = read_csv(path)
            self.assertIn("Industry [2]", headers)
            self.assertEqual(rows[0].values["Industry"], "Retail")
            self.assertEqual(rows[0].values["Industry [2]"], "Fashion")


class FakeResearcher:
    def research_employees(self, _: InputRow):
        return result(value=150), {"kind": "employees"}

    def research_locations(self, _: InputRow):
        return result(value=12), {"kind": "locations"}

    def research_revenue(self, _: InputRow):
        revenue = result(value=20_000_000)
        revenue.update(
            {
                "original_value": 20_000_000,
                "original_currency": "EUR",
                "fiscal_year": "2025",
                "metric": "revenue",
                "conversion_notes": "",
            }
        )
        return revenue, {"kind": "revenue"}


class FakeReviewResearcher(FakeResearcher):
    def research_employees(self, _: InputRow):
        return result(value=150, conflicting=True), {"kind": "employees"}


class RunnerTests(unittest.TestCase):
    def test_runner_exports_and_preserves_original_location(self) -> None:
        row = InputRow(
            record_id="record-1",
            source_row=2,
            values={
                "Company Name": "Example",
                "# Employees": "99",
                "Website": "https://example.com",
                "Company Linkedin Url": "https://linkedin.com/company/example",
                "Number of Retail Locations": "7",
            },
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            paths = run_stage1a(
                [row],
                list(row.values),
                output,
                FakeResearcher(),
            )
            self.assertTrue(paths["enriched"].exists())
            with paths["enriched"].open(newline="", encoding="utf-8-sig") as handle:
                enriched = next(csv.DictReader(handle))
            self.assertEqual(enriched["# Employees"], "99")
            self.assertEqual(enriched["Validated # Employees"], "150")
            self.assertEqual(enriched["Original Number of Retail Locations"], "7")
            self.assertEqual(enriched["Number of Retail Locations"], "12")
            self.assertEqual(enriched["Stage 1A Decision"], "PASS_1A")
            report = (
                output
                / "deliverables"
                / "Example"
                / "01 - Elegibilidad"
                / "Resultado Etapa 1.md"
            )
            self.assertTrue(report.exists())
            self.assertIn(
                "eligibility_decision: PENDING_1B",
                report.read_text(encoding="utf-8"),
            )

    def test_stage1b_exports_final_eligibility(self) -> None:
        row = InputRow(
            record_id="record-1b",
            source_row=2,
            values={
                "Company Name": "Example",
                "# Employees": "120",
                "Website": "https://example.com",
                "Company Linkedin Url": "https://linkedin.com/company/example",
                "Number of Retail Locations": "12",
            },
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            run_stage1a([row], list(row.values), output, FakeResearcher())
            paths = run_stage1b(
                [row], list(row.values), output, FakeResearcher()
            )
            with paths["enriched"].open(newline="", encoding="utf-8-sig") as handle:
                enriched = next(csv.DictReader(handle))
            self.assertEqual(enriched["Validated Annual Revenue EUR"], "20000000")
            self.assertEqual(enriched["Revenue Validation"], "VERIFIED_PASS")
            self.assertEqual(enriched["Eligibility Decision"], "ELIGIBLE")
            with paths["eligible"].open(newline="", encoding="utf-8-sig") as handle:
                eligible = list(csv.DictReader(handle))
            self.assertEqual(len(eligible), 1)
            report = (
                output
                / "deliverables"
                / "Example"
                / "01 - Elegibilidad"
                / "Resultado Etapa 1.md"
            ).read_text(encoding="utf-8")
            self.assertIn("eligibility_decision: ELIGIBLE", report)
            self.assertIn("| **Elegibilidad final** | | **ELIGIBLE** |", report)

    def test_single_review_can_receive_audited_human_override(self) -> None:
        row = InputRow(
            record_id="record-review",
            source_row=2,
            values={
                "Company Name": "Reviewed Example",
                "# Employees": "150",
                "Website": "https://example.com",
                "Company Linkedin Url": "https://linkedin.com/company/example",
                "Number of Retail Locations": "12",
            },
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            run_stage1a([row], list(row.values), output, FakeReviewResearcher())
            paths = run_stage1b(
                [row],
                list(row.values),
                output,
                FakeReviewResearcher(),
                approve_review=True,
            )
            with paths["enriched"].open(newline="", encoding="utf-8-sig") as handle:
                enriched = next(csv.DictReader(handle))
            self.assertEqual(enriched["Stage 1A Decision"], "REVIEW_REQUIRED")
            self.assertEqual(enriched["Stage 1A Override"], "YES")
            self.assertEqual(enriched["Eligibility Decision"], "ELIGIBLE")


if __name__ == "__main__":
    unittest.main()
