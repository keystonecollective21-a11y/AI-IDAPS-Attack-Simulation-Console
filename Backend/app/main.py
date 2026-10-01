import os

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.api.events import router as events_router
from app.api.reports import router as reports_router
from app.api.replay import router as replay_router
from app.api.scenarios import router as scenarios_router
from app.api.simulations import router as simulations_router
from app.database.database import init_db
from app.websocket.manager import manager


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# Server configuration
# ---------------------------------------------------------

HOST = os.getenv(
    "SIMULATION_HOST",
    "127.0.0.1"
)

PORT = int(
    os.getenv(
        "SIMULATION_PORT",
        "9000"
    )
)


# ---------------------------------------------------------
# Frontend configuration
# ---------------------------------------------------------

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    ""
).strip()


# ---------------------------------------------------------
# CORS configuration
# ---------------------------------------------------------

ALLOWED_ORIGINS = [
    # Local Vite development
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]


# Add production Vercel frontend when configured
if FRONTEND_URL:
    ALLOWED_ORIGINS.append(
        FRONTEND_URL.rstrip("/")
    )


# Remove duplicate origins
ALLOWED_ORIGINS = list(
    dict.fromkeys(ALLOWED_ORIGINS)
)


# ---------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="AI-IDAPS Attack Simulation Console",
    description=(
        "Professional synthetic cybersecurity "
        "attack simulation platform"
    ),
    version="2.0.0",
)


# ---------------------------------------------------------
# CORS middleware
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# API routers
# ---------------------------------------------------------

app.include_router(simulations_router)
app.include_router(events_router)
app.include_router(scenarios_router)
app.include_router(reports_router)
app.include_router(replay_router)


# ---------------------------------------------------------
# Startup
# ---------------------------------------------------------

@app.on_event("startup")
def startup():
    init_db()


# ---------------------------------------------------------
# Root endpoint
# ---------------------------------------------------------

@app.get("/")
def root():

    return {
        "application": "AI-IDAPS Attack Simulation Console",
        "version": "2.0.0",
        "status": "online",
    }


# ---------------------------------------------------------
# Health endpoint
# ---------------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "simulation-console",
    }


# ---------------------------------------------------------
# WebSocket endpoint
# ---------------------------------------------------------

@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):

    await manager.connect(websocket)

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        manager.disconnect(websocket)


# ---------------------------------------------------------
# Local development entry point
# ---------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=HOST,
        port=PORT,
        reload=True,
    )