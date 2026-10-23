# Incident Finder API

API for searching and analyzing incidents based on service logs.

## Tech Stack

- **Backend:** [Python 3.13](https://docs.python.org/3.13/), [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy 2.1](https://docs.sqlalchemy.org/en/21/)
- **Agent:** [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- **Database:** [PostgreSQL 18](https://www.postgresql.org/docs/18/index.html)
- **Tooling:** [uv](https://docs.astral.sh/uv/), [Docker](https://docs.docker.com/), [Docker Compose](https://docs.docker.com/compose/)

## Quick Start

```bash
git clone https://github.com/Cthupby/incident-finder-api.git
cd incident-finder-api
cp .env.example .env   # edit if necessary
docker compose up --build
```