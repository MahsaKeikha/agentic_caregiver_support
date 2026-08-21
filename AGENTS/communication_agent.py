class CommunicationAgent:
    name="communication"
    def run(self,c:dict)->dict:return {"communication":c.get("communication",{}),"structured":True}
