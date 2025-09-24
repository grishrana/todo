# Architecture (simple overview)

- Client sends HTTP requests to the FastAPI app.
- FastAPI routes are defined in `backend/app/main.py`.
- The app uses a database session (`Session_Dep`) to talk to PostgreSQL via SQLModel.
- Models (tables) are defined in `backend/app/models.py`.
- On startup, tables are created if missing and one example task is added.

## Request flow
1. Request comes to an endpoint (e.g., `POST /api/v1/create`).
2. FastAPI validates the request using the schema (`backend/app/schema/schema.py`).
3. The handler reads/writes tasks using the database session.
4. A JSON response is returned.

## Helpful links
- FastAPI docs: https://fastapi.tiangolo.com/
- SQLModel docs: https://sqlmodel.tiangolo.com/