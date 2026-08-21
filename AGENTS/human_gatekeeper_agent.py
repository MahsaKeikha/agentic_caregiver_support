class HumanGatekeeperAgent:
    name="human_gatekeeper"
    def run(self,c:dict)->dict:return {"approved":bool(c.get("human_approved",False)),"required":True}
