from fastapi.applications import FastAPI
from toolz import pipe

from app.ports.rest.routers import register_routers as register_routers
from app.config.environment import Settings
from app.adapters.database.configuration.sqlalchemy import connect_database, disconnect_database
from app.adapters.database.configuration.sqlalchemy import init_database as init_pgsql_db


def create_instance(settings: Settings) -> FastAPI:
    return FastAPI(
        debug="true",
        title="Houmer Tracking API",
        description="Houmer Tracking API",
        version="1.0",
    )


def init_databases(app: FastAPI) -> FastAPI:
    init_pgsql_db()
    return app


def register_events(app: FastAPI) -> FastAPI:
    app.on_event("startup")(connect_database)
    app.on_event("shutdown")(disconnect_database)

    return app


def register_middlewares(app: FastAPI) -> FastAPI:
    return app


def init_app(settings: Settings) -> FastAPI:
    app: FastAPI = pipe(
        settings,
        create_instance,
        init_databases,
        register_events,
        register_middlewares,
        register_routers,
    )
    return app
