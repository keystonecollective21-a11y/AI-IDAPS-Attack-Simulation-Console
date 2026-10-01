from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.database import Base


class SimulationEvent(Base):

    __tablename__ = "simulation_events"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    simulation_id = Column(String(100), index=True)

    event_type = Column(String(100), index=True)

    severity = Column(String(30))

    source_ip = Column(String(100))

    target = Column(String(200))

    mitre_technique = Column(String(100))

    risk_score = Column(Integer)

    details = Column(Text)

    ai_status = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )