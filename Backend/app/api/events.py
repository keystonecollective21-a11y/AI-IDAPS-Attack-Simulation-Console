from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.repositories import get_events

router = APIRouter(
    prefix="/api/events",
    tags=["Events"]
)


@router.get("")
def events(limit: int = 100):

    db = SessionLocal()

    try:

        records = get_events(db, limit)

        return [
            {
                "id": item.id,
                "timestamp": item.timestamp,
                "simulation_id": item.simulation_id,
                "event_type": item.event_type,
                "severity": item.severity,
                "source_ip": item.source_ip,
                "target": item.target,
                "mitre_technique": item.mitre_technique,
                "risk_score": item.risk_score,
                "ai_status": item.ai_status
            }
            for item in records
        ]

    finally:
        db.close()