from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.repositories import get_simulation_events

router = APIRouter(
    prefix="/api/replay",
    tags=["Replay"]
)


@router.get("/{simulation_id}")
def replay(simulation_id: str):

    db = SessionLocal()

    try:

        events = get_simulation_events(
            db,
            simulation_id
        )

        return [
            {
                "id": event.id,
                "timestamp": event.timestamp,
                "event_type": event.event_type,
                "severity": event.severity,
                "source_ip": event.source_ip,
                "target": event.target,
                "risk_score": event.risk_score,
                "mitre_technique": event.mitre_technique
            }
            for event in events
        ]

    finally:
        db.close()