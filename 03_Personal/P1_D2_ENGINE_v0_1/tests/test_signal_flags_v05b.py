import csv
from pathlib import Path

from p1_d2_engine.pilot_v05a import (
    build_flag_consistency_audit,
    recompute_signal_flags,
    signal_consistency_issues,
)


def evaluated_row(**overrides):
    row = {
        "ticker": "TEST",
        "status": "candidate",
        "candidate_d2": True,
        "d2_signal": True,
        "raw_d2_signal": False,
        "eligible_d2_signal": False,
        "universe_eligible": "True",
        "freshness_status": "fresh",
        "latest_fy_resolution_status": "resolved",
        "reason": "",
    }
    row.update(overrides)
    return row


def test_true_d2_true_universe_fresh_derives_eligible_signal_true():
    result = recompute_signal_flags(evaluated_row())
    assert result["raw_d2_signal"] is True
    assert result["eligible_d2_signal"] is True


def test_true_d2_unknown_universe_derives_eligible_signal_false():
    result = recompute_signal_flags(evaluated_row(universe_eligible="unknown"))
    assert result["raw_d2_signal"] is True
    assert result["eligible_d2_signal"] is False


def test_true_d2_nonfresh_derives_eligible_signal_false():
    result = recompute_signal_flags(evaluated_row(freshness_status="latest_fy_unresolved"))
    assert result["raw_d2_signal"] is True
    assert result["eligible_d2_signal"] is False


def test_false_d2_true_universe_fresh_derives_eligible_signal_false():
    result = recompute_signal_flags(
        evaluated_row(status="discard", candidate_d2=False, d2_signal=False)
    )
    assert result["raw_d2_signal"] is False
    assert result["eligible_d2_signal"] is False


def test_candidate_cannot_coexist_with_raw_false():
    result = evaluated_row()
    assert "candidate_requires_d2_and_raw_true" in signal_consistency_issues(result)


def test_aaon_like_revenue_unknown_to_resolved_recomputes_signal_flags():
    before_reconciliation = evaluated_row(
        ticker="AAON",
        universe_eligible="unknown",
        revenue_eligibility="unknown",
        raw_d2_signal=False,
        eligible_d2_signal=False,
    )
    after_reconciliation = dict(before_reconciliation)
    after_reconciliation.update(
        {
            "universe_eligible": "True",
            "revenue_eligibility": "True",
            "raw_d2_signal": False,
            "eligible_d2_signal": False,
        }
    )

    corrected = recompute_signal_flags(after_reconciliation)

    assert corrected["raw_d2_signal"] is True
    assert corrected["eligible_d2_signal"] is True
    assert before_reconciliation["raw_d2_signal"] is False


def test_revenue_merge_cannot_preserve_stale_raw_flag():
    d2_result = evaluated_row()
    d2_result.update({"d2_signal": True, "raw_d2_signal": False, "eligible_d2_signal": False})

    corrected = recompute_signal_flags(d2_result)

    assert corrected["raw_d2_signal"] is True
    assert corrected["eligible_d2_signal"] is True


def test_all_50_v05a_rows_pass_consistency_audit_after_regeneration():
    path = Path(__file__).parents[1] / "output/D2_results_v05A.csv"
    with path.open(newline="", encoding="utf-8") as source:
        frozen_rows = list(csv.DictReader(source))
    recomputed = [recompute_signal_flags(row) for row in frozen_rows]
    audit = build_flag_consistency_audit(recomputed)

    assert len(frozen_rows) == 50
    assert len(audit) == 50
    assert all(row["consistency_status"] == "consistent" for row in audit)
    assert sum(row["eligible_d2_signal"] is True for row in recomputed) == 3