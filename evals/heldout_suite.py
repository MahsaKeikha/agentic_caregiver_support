import json
from pathlib import Path

from orchestration.orchestrator import REQUIRED_GATES, evaluate_support


def base():
    context = {gate: True for gate in REQUIRED_GATES}
    context.update(
        urgent_red_flags=[], medication_change_requested=False, diagnosis_requested=False,
        caregiver_crisis=False, unresolved_conflicts=[], unresolved_questions=[],
        human_approval=True,
    )
    return context


SCENARIOS = [
    ("ready", {}, "READY_FOR_AUTHORIZED_SUPPORT"),
    ("identity_gap", {"care_recipient_identity_verified": False}, "BLOCKED"),
    ("urgent_red_flag", {"urgent_red_flags": ["acute change"]}, "BLOCKED"),
    ("medication_change", {"medication_change_requested": True}, "BLOCKED"),
    ("diagnosis_request", {"diagnosis_requested": True}, "BLOCKED"),
    ("caregiver_crisis", {"caregiver_crisis": True}, "BLOCKED"),
    ("privacy_gap", {"consent_and_privacy_confirmed": False}, "BLOCKED"),
    ("missing_human_approval", {"human_approval": False}, "BLOCKED"),
]


def main():
    rows = []
    for name, changes, expected in SCENARIOS:
        context = base()
        context.update(changes)
        actual = evaluate_support(context)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {"passed": passed, "total": len(rows), "pass_rate": passed / len(rows), "results": rows}
    Path("heldout-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if passed == len(rows) else 1)


if __name__ == "__main__":
    main()
