class HumanGatekeeperAgent:
    name = "human_gatekeeper"

    def run(self, context: dict) -> dict:
        return {
            "approved": bool(context.get("human_approved", False)),
            "required": True,
        }
