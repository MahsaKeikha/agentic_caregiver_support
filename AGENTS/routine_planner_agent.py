class RoutinePlannerAgent:
    name="routine_planner"
    def run(self,c:dict)->dict:return {"routine":c.get("routine",{}),"organized":True}
