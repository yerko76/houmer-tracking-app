# HOUM Tracking App

Houm tracking api permite realizar las siguientes capacidades de negocio:

1.  Agendar visitas para cada houmer, cada visita contendra una parada la cual el houmer visitara
2.  Actualizar la posicion actual del houmer
3.  Actualizar los estados de las paradas que el houmer visitara
4.  Realizar consultas sobre las paradas visitadas por el houmer usando distintos parametros de busqueda

## Documentation

[Arquitectura de componentes](documentation/architecture/hiight_level.md)
[Definicion de API](documentation/api/api.md)

## Tech Stack

El proyecto esta construido con las siguientes herramientas:

- Lenguaje: [Python 3.8+](https://www.python.org/)
- Manejador de paquetes: [Poetry](https://python-poetry.org/)
- Framework Web: [FastAPI](https://fastapi.tiangolo.com/)
- Web server: [Uvicorn](http://www.uvicorn.org/)
- Base de datos: [Postgres](https://www.postgresql.org/)
- Migraciones de BD: [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)

## Development

Para comenzar con el desarrollo se recomienda tener las siguientes herramientas instaladas

- [Python 3.8+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Plis](https://github.com/IcaliaLabs/plis)
- [Poetry](https://python-poetry.org/)

### Running the API

To run the API in development mode, follow these steps:

- Start a container with: `plis start --service-ports app ash`
- Inside the container run: `poetry install`
- Start the web server with: `poetry run web_server`
- Seed DB data with: `poetry run seeder`
- Run migrations with: `alembic upgrade head`
