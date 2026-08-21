class ObservationLoggerAgent:
    name="observation_logger"
    def run(self,c:dict)->dict:return {"observations":c.get("observations",[]),"logged":True}
