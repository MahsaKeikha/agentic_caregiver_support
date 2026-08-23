# F59 Agentic Caregiver Support

**Maturity:** L3 reference candidate  
**Version:** 1.0.0

A six-agent reference architecture for structured caregiver support across daily routines, observation logging, resource navigation, caregiver-to-clinician communication, escalation, and human oversight.

F59 is designed for family caregivers, professional caregivers, researchers, and engineering teams studying how multi-agent systems can reduce coordination burden without replacing medical judgment. The system helps organize what happened, what needs attention, what information should be communicated, and what support resources may be relevant.

It does not diagnose disease, interpret symptoms as a clinician, prescribe treatment, change medications, replace emergency services, or authorize medical decisions.

## Why caregiver support benefits from a multi-agent model

Caregiving is a continuous coordination problem. A caregiver may need to remember routines, observe changes, keep track of appointments, prepare questions, communicate with several professionals, locate community services, and recognize when a situation should be escalated.

The information itself may also be incomplete, subjective, or emotionally difficult to organize.

F59 separates these responsibilities into specialist roles:

```text
caregiving context
      |
      v
Routine Planner
      |
      v
Observation Logger
      |
      v
Resource Navigator
      |
      v
Communication Support
      |
      v
Escalation Review
      |
      v
Human Gatekeeper
```

This structure is intended to reduce cognitive and administrative burden while preserving human and clinical authority.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Routine Planner Agent | Organizes recurring caregiving activities and reminders | What routine tasks need to be tracked without changing the care plan? |
| Observation Logger Agent | Structures caregiver observations over time | What was directly observed, when did it occur, and what context should be preserved? |
| Resource Agent | Helps navigate approved support resources | What caregiver, community, educational, or service resources may be relevant? |
| Communication Agent | Formats concise caregiver updates for clinicians, family, or care teams | How can observations and questions be communicated clearly without adding unsupported conclusions? |
| Escalation Agent | Detects situations that require higher-priority human attention | Does the reported situation require contacting a clinician, care team, or emergency process? |
| Human Gatekeeper Agent | Preserves human decision authority | Has an appropriate human reviewed any consequential next step? |

## Repository structure

```text
AGENTS/
├── routine_planner_agent.py
├── observation_logger_agent.py
├── resource_agent.py
├── communication_agent.py
├── escalation_agent.py
└── human_gatekeeper_agent.py

SKILLS/
├── routine_planning.py
├── observation_logging.py
├── resource_navigation.py
├── caregiver_communication.py
└── escalation_review.py

TOOLS/
├── routine_tracker.py
├── observation_log_tool.py
├── resource_index.py
├── communication_formatter.py
└── escalation_router.py

benchmarks/
├── benchmark.py
└── RESULTS.md

evals/
├── evaluator.py
└── heldout_suite.py

orchestration/
memory/
observability/
schemas/
prompts/
config/
safety/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The repository separates agent reasoning from deterministic tools, shared state, observability, evaluation, and safety controls.

## Routine planning

The Routine Planner Agent supports organization of existing caregiving tasks. It should not invent or alter clinical instructions.

Examples of trackable activities include:

- meals and hydration reminders
- scheduled medications as already prescribed
- mobility or exercise activities already included in the care plan
- hygiene routines
- sleep and wake routines
- appointments
- transportation
- therapy sessions
- social activities
- caregiver shift coverage
- equipment checks
- household safety checks

`TOOLS/routine_tracker.py` provides the deterministic reference layer for routine state.

A routine record can include:

```text
routine_id
care_recipient_reference
activity
scheduled_time
source_of_instruction
status
completed_time
notes
caregiver_reference
```

The source of instruction matters. A task originating from a clinician, discharge plan, therapy plan, or family routine should not be presented as if the system itself prescribed it.

## Medication boundary

F59 may help a caregiver organize a medication schedule that already exists, but it must not:

- add a medication
- stop a medication
- change a dose
- change frequency
- recommend substituting one medication for another
- determine whether a missed dose should be taken
- interpret side effects as a diagnosis
- override pharmacy or clinician instructions

Medication questions should be directed to the appropriate clinician or pharmacist.

The system should preserve the difference between:

```text
PRESCRIBED INSTRUCTION
CAREGIVER OBSERVATION
QUESTION FOR CLINICIAN
```

These categories should never be silently merged.

## Observation logging

Caregiver observations can be extremely valuable when they are recorded accurately and consistently.

The Observation Logger Agent helps structure what the caregiver actually noticed without converting an observation into a diagnosis.

A useful record can include:

```text
observation_id
date_time
observer
context
observed_behavior_or_event
duration
frequency
possible_trigger_reported_by_caregiver
associated_routine
source
notes
```

Examples include:

- changes in sleep
- reduced appetite
- increased confusion
- repeated questions
- wandering behavior
- agitation
- falls or near-falls
- mobility changes
- hallucination-like experiences reported by the caregiver
- changes in participation
- unusual fatigue

The system should write, for example, "caregiver observed increased confusion after dinner" rather than converting that observation into a medical cause.

`TOOLS/observation_log_tool.py` provides the deterministic reference abstraction.

## Longitudinal patterns

Repeated observations can be organized over time to help caregivers and professionals notice trends.

Examples include:

```text
sleep disruption frequency
fall / near-fall count
meal completion pattern
nighttime wandering episodes
behavioral event frequency
appointment adherence
caregiver coverage gaps
```

Trend summaries should preserve uncertainty and source attribution. Correlation should not be represented as causation.

## Caregiver burden reduction

A central goal of F59 is reducing unnecessary cognitive load.

The system can support burden reduction by helping with:

- routine organization
- concise logs
- shared caregiver handoffs
- preparation for appointments
- resource discovery
- coordination of non-clinical tasks
- summarization of observations
- identifying unanswered questions
- reducing duplicated notes
- organizing respite and support options

The system should not frame the caregiver as merely a data source. Caregiver time, attention, fatigue, and capacity are part of the operating context.

## Caregiver handoff

When several people share caregiving responsibilities, structured handoffs can reduce information loss.

A handoff can include:

```text
current routine status
important observations
completed tasks
pending tasks
upcoming appointments
questions for care team
safety concerns already escalated
resource or coverage needs
```

A handoff should distinguish facts from impressions and should clearly identify unresolved items.

## Resource navigation

The Resource Agent helps organize non-diagnostic support options using `TOOLS/resource_index.py`.

Potential resource categories include:

- caregiver support groups
- respite care
- adult day programs
- transportation services
- home-care agencies
- social work resources
- caregiver education
- equipment resources
- meal support
- home-safety resources
- disease-specific nonprofit organizations
- local aging services
- financial or benefits navigation

Resource availability is location-dependent and changes over time. Production implementations should use current, authoritative resource directories and preserve source information.

The Resource Agent should not imply that a listed service is clinically appropriate, covered by insurance, currently available, or endorsed unless verified.

## Communication support

Caregivers often have extensive notes but limited time during a medical visit. The Communication Agent helps convert structured observations into concise updates and questions.

`TOOLS/communication_formatter.py` provides the reference formatting layer.

A clinician-facing summary can include:

```text
Reason for update
What changed
When it started
How often it occurs
What the caregiver directly observed
Relevant routine or environmental context
Questions for the care team
```

The system should avoid adding diagnostic labels that were not provided by a qualified professional.

For example:

```text
Preferred:
"Three nighttime wandering episodes were observed this week, compared with none last week."

Avoid:
"The patient's dementia has rapidly progressed."
```

The second statement is a clinical conclusion that cannot be inferred safely from the first observation alone.

## Preparing for appointments

F59 can help caregivers prepare useful information before a visit.

Examples include:

- recent changes
- frequency and timing of events
- missed or difficult routines
- falls or near-falls
- sleep changes
- appetite changes
- questions about medications
- questions about equipment
- questions about mobility
- questions about behavioral changes
- caregiver burden or coverage concerns

The system organizes these questions but does not answer them beyond its scope.

## Escalation model

The Escalation Agent identifies conditions that should not remain only in the organizational workflow.

`TOOLS/escalation_router.py` provides the routing abstraction.

Possible escalation categories include:

```text
ROUTINE FOLLOW-UP
CLINICIAN CONTACT RECOMMENDED
SAME-DAY HUMAN REVIEW
URGENT HUMAN REVIEW
EMERGENCY PROCESS
```

The exact routing logic should be defined by qualified professionals and local policy.

The system should not independently diagnose an emergency. When supplied information clearly indicates an emergency condition or the caregiver believes there is immediate danger, established emergency processes take priority over the agent workflow.

## Safety examples

Situations that should trigger human escalation may include reports of:

- a fall with possible injury
- sudden major change from baseline
- inability to safely transfer
- new severe confusion
- loss of consciousness
- breathing difficulty
- severe pain
- possible medication error
- missing person or unsafe wandering
- immediate risk of harm

The system should route and surface these reports, not interpret them as a definitive diagnosis.

## Human gatekeeper

The Human Gatekeeper Agent represents the authority boundary for consequential actions.

F59 must not autonomously:

- diagnose a condition
- determine disease progression
- prescribe treatment
- change medications
- modify a clinician's care plan
- decide whether hospitalization is necessary
- approve restraints
- make capacity or competency determinations
- authorize emergency intervention
- replace clinician, nurse, therapist, pharmacist, social worker, or emergency personnel

Its role is to ensure that important actions are reviewed by the appropriate human.

## Consent, identity, and privacy

Caregiver systems can contain sensitive information about both the care recipient and the caregiver.

Production systems should establish:

- who the care recipient is
- who the caregiver is
- whether the caregiver is authorized to access or share specific information
- what information may be shared with family members
- what information may be sent to clinicians or services
- consent and proxy/representative rules where applicable
- role-based access
- minimum-necessary data use
- retention and deletion policy
- secure authentication
- audit logging

A caregiver relationship alone should not be treated as unlimited authorization to access all health information.

## Data provenance

Every important piece of information should identify its source.

Examples include:

```text
caregiver report
clinician instruction
pharmacy instruction
care plan
hospital discharge instruction
sensor reading
calendar entry
resource directory
system-generated summary
```

This distinction is particularly important when several caregivers contribute information.

## Sensor and device integrations

F59 can be extended to accept observations from authorized devices such as:

- fall-detection systems
- activity monitors
- sleep monitors
- door sensors
- environmental sensors
- medication dispensers
- wearable devices

Device data should not automatically be treated as clinical truth. Production systems should preserve device identity, timestamp, data quality, uncertainty, and provenance.

An unusual sensor reading should generally be represented as a signal requiring review rather than a diagnosis.

## Shared memory and state

The `memory/` layer preserves coordination state across agents.

Useful state includes:

```text
care_recipient_reference
caregiver_reference
routine_state
observation_history
resource_requests
communication_drafts
escalation_state
human_review_state
unresolved_questions
```

Historical entries should remain distinguishable from current state.

Corrections should preserve an audit trail rather than silently replacing earlier caregiver observations.

## Observability

The `observability/` layer supports workflow traceability.

Useful operational metrics include:

- routines tracked
- overdue routine items
- observations logged
- communication summaries generated
- resource searches
- escalation events
- escalation acknowledgement time
- unresolved questions
- source-data failures
- human-review state

Metrics should support product and workflow improvement without becoming a hidden measure of caregiver performance.

Caregiver systems should avoid designs that create surveillance pressure or punish caregivers for incomplete logging.

## Fail-closed behavior

F59 should stop or escalate when critical information is missing or unsafe to infer.

Useful failure states include:

```text
CARE RECIPIENT IDENTITY UNCERTAIN
CAREGIVER AUTHORIZATION UNCLEAR
SOURCE OF INSTRUCTION UNKNOWN
MEDICATION QUESTION REQUIRES PROFESSIONAL REVIEW
OBSERVATION SOURCE UNKNOWN
RESOURCE INFORMATION UNVERIFIED
SAFETY ESCALATION REQUIRED
EMERGENCY PROCESS REQUIRED
HUMAN REVIEW REQUIRED
```

The system must never fabricate a caregiver observation, clinical instruction, medication order, clinician response, emergency assessment, resource availability, or human approval.

## End-to-end reference workflow

A typical F59 workflow follows this sequence:

1. Establish the care recipient and caregiver context.
2. Confirm authorization and privacy boundaries where relevant.
3. Load existing routines from trusted instructions.
4. Organize routine tasks without altering the care plan.
5. Record caregiver observations with time and provenance.
6. Organize longitudinal patterns without diagnosing them.
7. Identify caregiver resource needs.
8. Prepare concise updates and questions for the care team.
9. Detect situations requiring escalation.
10. Route escalation to the appropriate human or established process.
11. Preserve unresolved questions and provenance.
12. Keep consequential decisions with qualified humans.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run static checks and tests:

```bash
ruff check .
pytest -q
```

Run held-out evaluation:

```bash
python evals/heldout_suite.py
```

Run the example:

```bash
python examples/example_run.py
```

Run the main entry point:

```bash
python run.py
```

The repository includes CI under `.github/workflows/ci.yml`.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/benchmark.py
benchmarks/RESULTS.md
evals/evaluator.py
evals/heldout_suite.py
```

Evaluation should focus on safe caregiver support rather than diagnostic accuracy.

Useful dimensions include:

- routine preservation
- medication-boundary enforcement
- observation/source separation
- unsupported-diagnosis avoidance
- longitudinal-summary fidelity
- resource-source handling
- communication-summary fidelity
- escalation detection
- emergency-boundary enforcement
- authorization awareness
- privacy-boundary handling
- human-gate enforcement

Strong benchmark cases should include ambiguous observations, conflicting caregiver reports, missing source information, medication questions, resource uncertainty, and escalation scenarios.

## CI and reproducibility

Production systems should additionally test:

- caregiver identity and role handling
- authorization states
- duplicated observations
- corrected observations
- missing timestamps
- stale instructions
- medication-boundary cases
- sensor-data uncertainty
- resource-directory failures
- escalation-channel failures
- privacy filtering
- audit-log integrity

Version schemas, policies, prompts, escalation rules, resource sources, and benchmark cases so behavior can be reproduced after changes.

## L3 reference candidate

F59 follows the library's L3-oriented architecture through specialist agents, deterministic tools, held-out evaluation, observability, CI, safety boundaries, and explicit human authority.

This maturity designation describes the repository's engineering structure. It is not clinical validation, medical-device clearance, caregiver certification, evidence of improved clinical outcomes, or authorization for autonomous care decisions.

## Extending F59

Common extensions include:

- caregiver mobile applications
- shared family-care calendars
- clinician portal integrations
- EHR patient-message integration
- respite-care directories
- social-work resource directories
- transportation services
- home-care agency directories
- wearable integrations
- smart-home safety sensors
- medication reminder systems
- appointment preparation tools
- caregiver shift handoffs
- multilingual caregiver communication
- caregiver burden questionnaires
- care-plan document ingestion

New integrations should preserve provenance, privacy, authorization, uncertainty, and human review.

## Example use cases

F59 can serve as a reference for:

- family caregiver organization
- dementia and cognitive-aging support workflows
- Parkinson's caregiving coordination
- aging-in-place support
- post-discharge caregiver organization
- shared family caregiving
- caregiver research tools
- home-monitoring support systems
- clinician-caregiver communication preparation
- respite and resource navigation

These examples describe workflow support, not diagnosis or treatment.

## Design principles

1. Reduce caregiver administrative burden without replacing caregiver judgment.
2. Keep direct observations separate from clinical conclusions.
3. Preserve the source of every instruction and observation.
4. Never change medications or treatment plans autonomously.
5. Make routine coordination simple and auditable.
6. Support concise communication with care teams.
7. Treat caregiver capacity and burden as part of the workflow context.
8. Escalate safety concerns rather than attempting diagnosis.
9. Protect both caregiver and care-recipient privacy.
10. Keep consequential medical and emergency decisions with qualified humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository's citation metadata when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F59 as a caregiver-support and multi-agent architecture reference. Validate routines, resource directories, escalation rules, privacy controls, authorization, communication workflows, sensor integrations, and human-review boundaries against the real caregiving environment before deployment. Final clinical, medication, treatment, and emergency decisions remain with qualified professionals and accountable humans.