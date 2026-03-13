#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

DIMENSIONS = ["correctness", "relevance", "actionability", "risk", "tool_reliability"]


def load(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def mean(vals: list[float]) -> float:
    return round(sum(vals) / len(vals), 2) if vals else 0.0


def evaluate(cases: list[dict]) -> dict:
    if not cases:
        return {
            "total_cases": 0,
            "dimension_averages": {d: 0.0 for d in DIMENSIONS},
            "overall_score": 0.0,
            "go_no_go": "No-Go",
            "reason": "No evaluation cases provided",
        }

    by_dim: dict[str, list[float]] = {d: [] for d in DIMENSIONS}
    critical_cases = [c for c in cases if str(c.get("risk_level", "low")).lower() == "high"]

    for c in cases:
        scores = c.get("scores", {})
        for d in DIMENSIONS:
            v = float(scores.get(d, 0))
            if v < 1:
                v = 1
            if v > 5:
                v = 5
            by_dim[d].append(v)

    dim_avg = {d: mean(v) for d, v in by_dim.items()}
    overall = mean(list(dim_avg.values()))

    critical_min = 5.0
    if critical_cases:
        mins = []
        for c in critical_cases:
            s = c.get("scores", {})
            mins.append(min(float(s.get(d, 1)) for d in DIMENSIONS))
        critical_min = round(min(mins), 2)

    if overall >= 4.2 and critical_min >= 4.0:
        verdict = "Go"
    elif overall >= 3.4 and critical_min >= 3.0:
        verdict = "Conditional Go"
    else:
        verdict = "No-Go"

    return {
        "total_cases": len(cases),
        "critical_cases": len(critical_cases),
        "dimension_averages": dim_avg,
        "overall_score": overall,
        "critical_min_score": critical_min,
        "go_no_go": verdict,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic scorer for Agent Evals Lab")
    ap.add_argument("--input", required=True, help="Path to evaluation cases JSON")
    ap.add_argument("--out", default="", help="Optional output file path")
    args = ap.parse_args()

    data = load(args.input)
    cases = data.get("cases", data if isinstance(data, list) else [])
    result = evaluate(cases)

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
