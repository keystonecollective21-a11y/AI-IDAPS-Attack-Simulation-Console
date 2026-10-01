import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "AI_IDAPS_BACKEND_URL",
    "http://127.0.0.1:8000"
).rstrip("/")

ENDPOINT = os.getenv(
    "AI_IDAPS_EVENT_ENDPOINT",
    "/api/security/events"
)

EVENT_URL = BASE_URL + ENDPOINT


def send_event(event: dict):
    try:
        response = requests.post(
            EVENT_URL,
            json=event,
            timeout=5
        )

        if response.ok:
            try:
                data = response.json()

                # Project 1 returns:
                # {
                #   "success": true,
                #   "message": "...",
                #   "event": {...}
                # }

                processed_event = data.get(
                    "event",
                    event
                )

            except ValueError:
                processed_event = event

            return {
                "success": True,
                "status_code": response.status_code,
                "event": processed_event
            }

        return {
            "success": False,
            "status_code": response.status_code,
            "event": event,
            "response": response.text[:500]
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "status_code": None,
            "event": event,
            "response": str(error)
        }