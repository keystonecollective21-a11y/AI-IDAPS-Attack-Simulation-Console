from fastapi import APIRouter

from app.simulation.engine import engine

router = APIRouter(
    prefix="/api/simulations",
    tags=["Simulations"]
)


@router.post("/start/{attack_type}")
async def start_simulation(attack_type: str):

    started = await engine.start(attack_type)

    return {
        "success": started,
        "running": engine.running,
        "attack_type": engine.attack_type,
        "simulation_id": engine.simulation_id
    }


@router.post("/stop")
async def stop_simulation():

    await engine.stop()

    return {
        "success": True,
        "running": False
    }


@router.get("/status")
async def simulation_status():

    return {
        "running": engine.running,
        "attack_type": engine.attack_type,
        "simulation_id": engine.simulation_id,
        "event_count": engine.event_count
    }