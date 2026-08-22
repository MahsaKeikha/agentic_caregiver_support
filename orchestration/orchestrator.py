from __future__ import annotations

from typing import Any

from AGENTS.communication_agent import CommunicationAgent
from AGENTS.escalation_agent import EscalationAgent
from AGENTS.human_gatekeeper_agent import HumanGatekeeperAgent
from AGENTS.observation_logger_agent import ObservationLoggerAgent
from AGENTS.resource_agent import ResourceAgent
from AGENTS.routine_planner_agent import RoutinePlannerAgent


REQUIRED_GATES = {
    "care_recipient_identity_verified": "care recipient identity is not verified",
    "caregiver_role_confirmed": "caregiver role or authority is not confirmed",
    "consent_and_privacy_confirmed": "consent or privacy requirements are incomplete",
    "care_plan_current": "care plan is not current",
    "handoff_complete": "care handoff is incomplete",
    "observation_log_complete": "care observations are incomplete",
    "medication_boundaries_confirmed": "medication boundaries are not confirmed",
    "fall_safety_reviewed": "fall-safety review is incomplete",
    "wandering_safety_reviewed": "wandering safety review is incomplete",
    "infection_control_reviewed": "infection-control review is incomplete",
    "escalation_path_ready": "clinical or emergency escalation path is not ready",
    "respite_plan_reviewed": "caregiver respite/support plan has not been reviewed",
}


def _specialists(context: dict[str, Any]) -> dict[str, Any]:
    agents = [
        RoutinePlannerAgent(),
        ObservationLoggerAgent(),
        ResourceAgent(),
        CommunicationAgent(),
        EscalationAgent(),
        HumanGatekeeperAgent(),
    ]
    return {agent.name: agent.run(context) for agent in agents}


def evaluate_support(context: dict[str, Any]) -> dict[str, Any]:
    blockers = [
        message
        for gate, message in REQUIRED_GATES.items()
        if not context.get(gate, False)
    ]
    if context.get("urgent_red_flags"):
        blockers.append("urgent health or safety red flags require qualified escalation")
    if context.get("medication_change_requested"):
        blockers.append("autonomous medication changes are outside this workflow")
    if context.get("diagnosis_requested"):
        blockers.append("autonomous diagnosis is outside this workflow")
    if context.get("caregiver_crisis"):
        blockers.append("caregiver crisis requires immediate human support and escalation")
    if context.get("unresolved_conflicts"):
        blockers.append("unresolved care-team or family conflicts remain")
    if context.get("unresolved_questions"):
        blockers.append("unresolved care or clinical questions remain")
    if context.get("human_approval") is not True:
        blockers.append("authorized qualified human oversight is required")

    return {
        "status": "READY_FOR_AUTHORIZED_SUPPORT" if not blockers else "BLOCKED",
        "blockers": blockers,
        "human_approval_required": True,
        "autonomous_clinical_authority": False,
        "notes": (
            "This system supports caregiver organization, observations, communication, "
            "resources, and escalation. It does not diagnose, prescribe, change medications, "
            "or replace qualified clinical or emergency judgment."
        ),
    }


def run_workflow(context: dict[str, Any]) -> dict[str, Any]:
    return {"specialists": _specialists(context), "governance": evaluate_support(context)}
