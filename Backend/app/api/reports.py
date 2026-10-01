from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.repositories import get_events

router = APIRouter(
    prefix="/api/reports",
    tags=["Reports"]
)


@router.get("/summary")
def report_summary():

    db = SessionLocal()

    try:

        events = get_events(db, 10000)

        total = len(events)

        high_risk = len([
            event
            for event in events
            if event.risk_score >= 70
        ])

        critical = len([
            event
            for event in events
            if event.severity == "CRITICAL"
        ])

        return {
            "total_events": total,
            "high_risk_events": high_risk,
            "critical_events": critical
        }

    finally:
        db.close()