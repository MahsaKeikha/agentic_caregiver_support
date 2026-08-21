def evaluate(r:dict)->dict:
    required=["routine_planner","observation_logger","resource","communication","escalation","human_gatekeeper"]
    m=[x for x in required if x not in r]
    return {"passed":not m,"missing":m}
