from __future__ import annotations

import json
from pathlib import Path

from p1_d2_engine.d2_engine import evaluate_company
from p1_d2_engine.io_utils import write_rows


ROOT = Path(__file__).resolve().parents[1]
facts = json.loads(
    (ROOT / "tests" / "fixtures" / "companyfacts_candidate.json").read_text(encoding="utf-8")
)
result, provenance = evaluate_company("TEST", 1, facts, "Synthetic Test Co")
out = ROOT / "output_demo"
out.mkdir(exist_ok=True)
write_rows(out / "D2_results_demo.csv", [result.to_row()])
write_rows(out / "D2_provenance_demo.csv", [f.provenance_row("TEST", 1) for f in provenance])
(out / "README.md").write_text(
    "# Synthetic demo output\n\n"
    "This is not market data. It exercises the full D2 calculation and provenance path with a controlled fixture.\n",
    encoding="utf-8",
)
print(result.to_row())
