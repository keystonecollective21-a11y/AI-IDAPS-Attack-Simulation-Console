import asyncio
import os
from uuid import uuid4

from dotenv import load_dotenv

from app.database.database import SessionLocal
from app.database.repositories import save_event
from app.integration.ai_idaps_client import send_event
from app.integration.event_mapper import prepare_event
from app.simulation.event_generator import generate_event
from app.websocket.manager import manager

load_dotenv()

INTERVAL = float(
    os.getenv("SIMULATION_INTERVAL", "1")
)


class SimulationEngine:

    def __init__(self):
        self.running = False
        self.attack_type = None
        self.simulation_id = None
        self.event_count = 0

    async def start(self, attack_type: str):

        if self.running:
            return False

        self.running = True
        self.attack_type = attack_type
        self.simulation_id = str(uuid4())
        self.event_count = 0

        asyncio.create_task(
            self._run()
        )

        return True

    async def _run(self):

        while self.running:

            try:

                # Generate synthetic event
                event = generate_event(
                    self.attack_type
                )

                # Add simulation metadata
                event = prepare_event(
                    event,
                    self.simulation_id
                )

                # Send to Project 1
                ai_result = send_event(
                    event
                )

                if ai_result["success"]:

                    # IMPORTANT:
                    # Use the processed event returned
                    # by Project 1
                    authoritative_event = (
                        ai_result.get("event")
                        or event
                    )

                    authoritative_event[
                        "ai_status"
                    ] = "DELIVERED"

                    authoritative_event[
                        "simulation_attack_type"
                    ] = self.attack_type

                else:

                    authoritative_event = event

                    authoritative_event[
                        "ai_status"
                    ] = "AI-IDAPS_OFFLINE"

                # Save simulation event
                db = SessionLocal()

                try:

                    save_event(
                        db,
                        authoritative_event
                    )

                finally:

                    db.close()

                self.event_count += 1

                # REAL-TIME broadcast
                await manager.broadcast({
                    "type": "security_event",
                    "data": authoritative_event,
                    "stats": {
                        "event_count":
                            self.event_count,
                        "running":
                            self.running,
                        "attack_type":
                            self.attack_type,
                        "simulation_id":
                            self.simulation_id
                    }
                })

                print(
                    f"[REALTIME] "
                    f"{self.attack_type} "
                    f"event #{self.event_count}"
                )

            except Exception as error:

                print(
                    "SIMULATION ERROR:",
                    error
                )

            await asyncio.sleep(
                INTERVAL
            )

    async def stop(self):

        self.running = False

        await manager.broadcast({
            "type": "simulation_status",
            "running": False,
            "simulation_id":
                self.simulation_id,
            "event_count":
                self.event_count
        })


engine = SimulationEngine()