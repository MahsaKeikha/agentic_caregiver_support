from AGENTS.routine_planner_agent import RoutinePlannerAgent
from AGENTS.observation_logger_agent import ObservationLoggerAgent
from AGENTS.resource_agent import ResourceAgent
from AGENTS.communication_agent import CommunicationAgent
from AGENTS.escalation_agent import EscalationAgent
from AGENTS.human_gatekeeper_agent import HumanGatekeeperAgent

def run_workflow(c:dict)->dict:
    agents=[RoutinePlannerAgent(),ObservationLoggerAgent(),ResourceAgent(),CommunicationAgent(),EscalationAgent(),HumanGatekeeperAgent()]
    return {a.name:a.run(c) for a in agents}
