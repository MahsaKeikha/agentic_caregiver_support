# Agentic Caregiver Support

F59 standalone multi-agent caregiver workflow support system.

## Agents

- [`routine_planner_agent.py`](AGENTS/routine_planner_agent.py)
- [`observation_logger_agent.py`](AGENTS/observation_logger_agent.py)
- [`resource_agent.py`](AGENTS/resource_agent.py)
- [`communication_agent.py`](AGENTS/communication_agent.py)
- [`escalation_agent.py`](AGENTS/escalation_agent.py)
- [`human_gatekeeper_agent.py`](AGENTS/human_gatekeeper_agent.py)

## Tools

- [`routine_tracker.py`](TOOLS/routine_tracker.py)
- [`observation_log_tool.py`](TOOLS/observation_log_tool.py)
- [`resource_index.py`](TOOLS/resource_index.py)
- [`communication_formatter.py`](TOOLS/communication_formatter.py)
- [`escalation_router.py`](TOOLS/escalation_router.py)

## Skills

- [`routine_planning.py`](SKILLS/routine_planning.py)
- [`observation_logging.py`](SKILLS/observation_logging.py)
- [`resource_navigation.py`](SKILLS/resource_navigation.py)
- [`caregiver_communication.py`](SKILLS/caregiver_communication.py)
- [`escalation_review.py`](SKILLS/escalation_review.py)

Supporting layers include orchestration, memory, state, schemas, prompts, config, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

This system supports caregiver organization and observation logging. It does not diagnose, prescribe, replace emergency processes, or replace qualified clinical judgment.
