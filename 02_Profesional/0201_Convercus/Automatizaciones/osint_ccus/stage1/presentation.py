"""Presentation rules for original versus effective Stage 1 decisions."""

from __future__ import annotations

from typing import Any


def effective_criterion_decision(
    eligibility: dict[str, Any],
    criterion: str,
) -> str:
    """Return the decision that is actually in force for a user-facing report."""
    decision = eligibility.get("decision") or {}
    final = eligibility.get("final_decision") or {}
    stored = str(decision.get(f"{criterion}_decision") or "")
    consensus = (eligibility.get(criterion) or {}).get("threshold_consensus")

    if consensus == "all_above":
        return "VERIFIED_PASS"
    if consensus == "all_at_or_below":
        return "VERIFIED_FAIL"
    if consensus == "crosses":
        return "CONFLICTING"

    if (
        final.get("stage1a_override") is True
        and final.get("stage1a_effective_decision") == "PASS_1A"
        and stored in {"CONFLICTING", "UNKNOWN"}
    ):
        return "VERIFIED_PASS (revisión humana)"
    return stored


def original_decision_note(eligibility: dict[str, Any]) -> str | None:
    final = eligibility.get("final_decision") or {}
    original = final.get("stage1a_original_decision")
    effective = final.get("stage1a_effective_decision")
    if original and effective and original != effective:
        return (
            f"La decisión automática original fue `{original}` y la decisión "
            f"efectiva, tras revisión humana, es `{effective}`."
        )
    return None
