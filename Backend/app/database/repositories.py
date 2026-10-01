import json

from sqlalchemy.orm import Session

from app.database.models import SimulationEvent


def save_event(db: Session, event: dict):

    record = SimulationEvent(
        simulation_id=event.get("simulation_id"),
        event_type=event.get("event_type"),
        severity=event.get("severity"),
        source_ip=event.get("source_ip"),
        target=event.get("target"),
        mitre_technique=event.get("mitre_technique"),
        risk_score=event.get("risk_score", 0),
        details=json.dumps(event.get("details", {})),
        ai_status=event.get("ai_status", "PENDING")
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_events(db: Session, limit: int = 100):

    return (
        db.query(SimulationEvent)
        .order_by(SimulationEvent.id.desc())
        .limit(limit)
        .all()
    )


def get_simulation_events(
    db: Session,
    simulation_id: str
):

    return (
        db.query(SimulationEvent)
        .filter(
            SimulationEvent.simulation_id == simulation_id
        )
        .order_by(SimulationEvent.id.asc())
        .all()
    )