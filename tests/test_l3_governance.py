from orchestration.orchestrator import REQUIRED_GATES, evaluate_support


def ready_context():
    context = {gate: True for gate in REQUIRED_GATES}
    context.update(
        urgent_red_flags=[],
        medication_change_requested=False,
        diagnosis_requested=False,
        caregiver_crisis=False,
        unresolved_conflicts=[],
        unresolved_questions=[],
        human_approval=True,
    )
    return context


def test_ready_support_requires_all_gates_and_human_approval():
    result = evaluate_support(ready_context())
    assert result["status"] == "READY_FOR_AUTHORIZED_SUPPORT"
    assert result["blockers"] == []
    assert result["autonomous_clinical_authority"] is False


def test_each_required_gate_fails_closed():
    for gate in REQUIRED_GATES:
        context = ready_context()
        context[gate] = False
        result = evaluate_support(context)
        assert result["status"] == "BLOCKED", gate


def test_urgent_red_flags_require_escalation():
    context = ready_context()
    context["urgent_red_flags"] = ["acute change"]
    assert evaluate_support(context)["status"] == "BLOCKED"


def test_medication_and_diagnosis_requests_are_blocked():
    context = ready_context()
    context["medication_change_requested"] = True
    context["diagnosis_requested"] = True
    result = evaluate_support(context)
    assert result["status"] == "BLOCKED"
    assert len(result["blockers"]) >= 2


def test_caregiver_crisis_requires_human_support():
    context = ready_context()
    context["caregiver_crisis"] = True
    assert evaluate_support(context)["status"] == "BLOCKED"


def test_human_approval_is_required():
    context = ready_context()
    context["human_approval"] = False
    assert evaluate_support(context)["status"] == "BLOCKED"
