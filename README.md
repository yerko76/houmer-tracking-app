# HOUM Tracking App

Houm tracking api permite realizar las siguientes capacidades de negocio:

1.  Agendar visitas para cada houmer, cada visita contendra una parada la cual el houmer visitara
2.  Actualizar la posicion actual del houmer
3.  Actualizar los estados de las paradas que el houmer visitara
4.  Realizar consultas sobre las paradas visitadas por el houmer usando distintos parametros de busqueda

Supuestos: Se supone que la carga de lugares con sus cordenadas es responsabilidad de otro servicio, y se asume que la data existe, es por esto que se usa un seeder para cargar data de prueba.
Se asume que estamos en un contexto de seguridad por lo cual no se desarrollan componentes para validar jwt/oauth/open id connect

## Documentation

- Descripcion de arquitectura de alto nivel, arquitectura de componentes y estructura de proyecto [Arquitectura de componentes](documentation/architecture/hiight_level.md)
- Descripcion y definicion de la API [Definicion de API](documentation/api/api.md)
- Persistencia y diagrama de ER [DB](documentation/persistence/persistence.md)

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

### Running the API in local env

Revisar las variables de ambiente en el archivo .env

- Instalar librerias

```console
poetry install
```

- Iniciar el contenedor de postgres

```console
plis start pgsql-db
```

- ejecutar migraciones con alembic.

```console
poetry run alembic upgrade head
```

- cargar data de prueba

```console
poetry run seeder
```

- Iniciar el servidor web

```console
poetry run web_server
```

- Revisar si la app esta corriendo de forma correcta

```console
curl -X 'GET' \
  'http://localhost:8000/status' \
  -H 'accept: application/json'
```

Para ejecutar todo desde docker

- Levantar todos los contenedores

```console
plis start
```

- Revisar si la app esta corriendo de forma correcta

```console
curl -X 'GET' \
  'http://localhost:8000/status' \
  -H 'accept: application/json'
```
