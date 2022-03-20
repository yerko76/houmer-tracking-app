from app.ports.rest.routers.health import health
from app.ports.rest.routers.visits import visit
from app.ports.rest.routers.stops import stop
from fastapi.applications import FastAPI


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(health.router)
    app.include_router(visit.router, prefix="/api/visits")
    app.include_router(stop.router, prefix="/api/visits")
    return app
