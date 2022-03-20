# APP

## Description

## Tech Stack

This project is comprised of the following languages and libraries:

- Language: [Python 3.8+](https://www.python.org/)
- Package management: [Poetry](https://python-poetry.org/)
- Web framework: [FastAPI](https://fastapi.tiangolo.com/)
- Production web server: [Uvicorn](http://www.uvicorn.org/)
- Relational database: [Postgres](https://www.postgresql.org/)
- Relational database async support: [databases](https://www.encode.io/databases/)
- Relational database migrations: [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- Relational ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Functional programming utilities: [Toolz](https://toolz.readthedocs.io/en/latest/)
- Data parsing and validation: [Pydantic](https://pydantic-docs.helpmanual.io/)

Auxiliary libraries were omitted but can be found in the [pyproject](https://github.com/GArmane/python-fastapi-hex-todo/blob/master/pyproject.toml) file.

## Development

To start development it is recommended to have these utilities installed in a local development machine:

- [Python 3.8+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Plis](https://github.com/IcaliaLabs/plis)

For better development experience, it is recommended these tools:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Poetry](https://python-poetry.org/)

Be certain that you are installing Poetry with the correct version of Python in your machine, that is, Python 3.

This project is already configured with VS Code IDE in mind. To have access of tools and code analysis utilities, you only need to install the project dependencies locally with `poetry install` and to open the project workspace file on VS Code.

The IDE should be automatically configured with standard rules and options for optimal development experience.

### Running the API

To run the API in development mode, follow these steps:

- Start a container with: `plis start --service-ports app ash`
- Inside the container run: `poetry install`
- Start the web server with: `poetry run web_server`
- Seed DB data with: `poetry run seeder`
- Run migrations with: `alembic upgrade head`

