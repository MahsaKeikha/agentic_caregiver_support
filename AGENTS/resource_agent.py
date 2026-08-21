class ResourceAgent:
    name="resource"
    def run(self,c:dict)->dict:return {"resource_topics":c.get("resource_topics",[]),"review_required":True}
