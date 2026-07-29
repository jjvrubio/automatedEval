"""Deterministic eligibility policy.

The model researches and structures evidence. This module alone decides whether
the strict employee and location thresholds are met.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class CriterionDecision(str, Enum):
    VERIFIED_PASS = "VERIFIED_PASS"
    VERIFIED_FAIL = "VERIFIED_FAIL"
    UNKNOWN = "UNKNOWN"
    CONFLICTING = "CONFLICTING"


class StageDecision(str, Enum):
    PASS_1A = "PASS_1A"
    FAIL_1A = "FAIL_1A"
    ELIGIBLE = "ELIGIBLE"
    INELIGIBLE = "INELIGIBLE"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"


@dataclass(frozen=True)
class PolicyResult:
    decision: CriterionDecision
    reason: str


@dataclass(frozen=True)
class StagePolicyResult:
    decision: StageDecision
    reason: str


def _as_number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def evaluate_criterion(research: dict[str, Any], threshold: float) -> PolicyResult:
    """Evaluate a strict ``value > threshold`` rule from structured research."""
    evidence = research.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return PolicyResult(
            CriterionDecision.UNKNOWN,
            "No existe evidencia recuperable para aplicar el umbral.",
        )

    identity_status = research.get("identity_status")
    if identity_status == "conflicting":
        return PolicyResult(
            CriterionDecision.CONFLICTING,
            "Las fuentes no permiten resolver de forma consistente la identidad.",
        )
    if identity_status != "matched":
        return PolicyResult(
            CriterionDecision.UNKNOWN,
            "La identidad de la entidad investigada no está confirmada.",
        )

    threshold_consensus = research.get("threshold_consensus")
    if threshold_consensus == "all_above":
        return PolicyResult(
            CriterionDecision.VERIFIED_PASS,
            f"Todas las fuentes creíbles sitúan el valor por encima de {threshold:g}.",
        )
    if threshold_consensus == "all_at_or_below":
        return PolicyResult(
            CriterionDecision.VERIFIED_FAIL,
            f"Todas las fuentes creíbles sitúan el valor en o por debajo de {threshold:g}.",
        )
    if threshold_consensus == "crosses":
        return PolicyResult(
            CriterionDecision.CONFLICTING,
            f"Las fuentes creíbles quedan a ambos lados del umbral {threshold:g}.",
        )

    if research.get("conflicting") is True:
        return PolicyResult(
            CriterionDecision.CONFLICTING,
            "Las fuentes recuperadas presentan cifras incompatibles.",
        )

    value_type = str(research.get("value_type") or "unknown")
    value = _as_number(research.get("value"))
    lower = _as_number(research.get("lower_bound"))
    upper = _as_number(research.get("upper_bound"))

    if value_type == "exact" and value is not None:
        if value > threshold:
            return PolicyResult(
                CriterionDecision.VERIFIED_PASS,
                f"Valor exacto {value:g} superior al umbral estricto {threshold:g}.",
            )
        return PolicyResult(
            CriterionDecision.VERIFIED_FAIL,
            f"Valor exacto {value:g} no superior al umbral estricto {threshold:g}.",
        )

    if value_type == "minimum" and lower is not None:
        if lower > threshold:
            return PolicyResult(
                CriterionDecision.VERIFIED_PASS,
                f"Mínimo probado {lower:g} superior al umbral estricto {threshold:g}.",
            )
        return PolicyResult(
            CriterionDecision.UNKNOWN,
            f"El mínimo probado {lower:g} no permite decidir frente a {threshold:g}.",
        )

    if value_type == "range" and lower is not None and upper is not None:
        if lower > threshold:
            return PolicyResult(
                CriterionDecision.VERIFIED_PASS,
                f"Todo el rango {lower:g}-{upper:g} supera {threshold:g}.",
            )
        if upper <= threshold:
            return PolicyResult(
                CriterionDecision.VERIFIED_FAIL,
                f"Todo el rango {lower:g}-{upper:g} queda en o bajo {threshold:g}.",
            )
        return PolicyResult(
            CriterionDecision.UNKNOWN,
            f"El rango {lower:g}-{upper:g} cruza el umbral {threshold:g}.",
        )

    if value_type == "estimate" and value is not None:
        return PolicyResult(
            CriterionDecision.UNKNOWN,
            f"La estimación {value:g} no se considera suficiente para una decisión automática.",
        )

    return PolicyResult(
        CriterionDecision.UNKNOWN,
        "La investigación no produjo una cifra exacta, mínima o acotada utilizable.",
    )


def evaluate_final_eligibility(
    stage1a: StagePolicyResult,
    revenue: PolicyResult,
) -> StagePolicyResult:
    """Combine an effective Stage 1A pass with the revenue criterion."""
    if stage1a.decision != StageDecision.PASS_1A:
        return StagePolicyResult(
            StageDecision.REVIEW_REQUIRED,
            f"La puerta 1A no está aprobada: {stage1a.decision.value}.",
        )
    if revenue.decision == CriterionDecision.VERIFIED_PASS:
        return StagePolicyResult(
            StageDecision.ELIGIBLE,
            "Supera 1A y acredita facturación estrictamente superior a 15M EUR.",
        )
    if revenue.decision == CriterionDecision.VERIFIED_FAIL:
        return StagePolicyResult(
            StageDecision.INELIGIBLE,
            "Supera 1A, pero no acredita facturación estrictamente superior a 15M EUR.",
        )
    return StagePolicyResult(
        StageDecision.REVIEW_REQUIRED,
        f"Facturación: {revenue.decision.value}.",
    )


def evaluate_stage1a(
    employees: PolicyResult,
    locations: PolicyResult,
) -> StagePolicyResult:
    """Combine employees and locations with an AND rule."""
    decisions = {employees.decision, locations.decision}

    if CriterionDecision.VERIFIED_FAIL in decisions:
        return StagePolicyResult(
            StageDecision.FAIL_1A,
            f"Empleados: {employees.decision.value}. Ubicaciones: {locations.decision.value}.",
        )

    if decisions == {CriterionDecision.VERIFIED_PASS}:
        return StagePolicyResult(
            StageDecision.PASS_1A,
            "Supera simultáneamente >100 empleados y >10 puntos de venta o servicio.",
        )

    return StagePolicyResult(
        StageDecision.REVIEW_REQUIRED,
        f"Empleados: {employees.decision.value}. Ubicaciones: {locations.decision.value}.",
    )
