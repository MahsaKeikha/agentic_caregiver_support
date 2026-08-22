class ResourceAgent:
    name = "resource"

    def run(self, context: dict) -> dict:
        return {
            "resource_topics": context.get("resource_topics", []),
            "review_required": True,
        }
