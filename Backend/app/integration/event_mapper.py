from uuid import uuid4


def prepare_event(event: dict, simulation_id: str | None = None):

    event["simulation"] = True

    event["source"] = (
        "AI-IDAPS-Attack-Simulation-Console"
    )

    event["simulation_id"] = (
        simulation_id or str(uuid4())
    )

    event["ai_status"] = "SENT_TO_AI_IDAPS"

    return event