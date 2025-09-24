# Smart Todo

A simple backend API built with FastAPI and SQLModel to manage todo tasks.

## What you can do
- Create a task
- See all tasks
- See one task by id
- Update a task
- Delete a task

## Tech used
- FastAPI (web framework)
- SQLModel (models and DB)
- PostgreSQL (database)

## Quick start
1) Install Python 3.11+ and PostgreSQL
2) Clone this repo
3) Create a virtual environment and install deps
```
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn sqlmodel psycopg[binary] python-dotenv
```
4) Create a PostgreSQL database named `smart_todo`
```
createdb smart_todo
```
5) Copy `.env.example` to `.env` and fill values
```
DB_USER=your_db_user
DB_PASS=your_db_password
```
6) Run the API
```
uvicorn backend.app.main:app --reload
```
7) Open the docs in your browser
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example request
Create a task:
```
curl -X POST http://127.0.0.1:8000/api/v1/create \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Watch a tutorial",
    "priority": "medium",
    "end_date": "2025-10-25T00:00:00Z"
  }'
```

## Project structure
- backend/app/main.py — API routes
- backend/app/models.py — database models
- backend/app/schema/schema.py — request/response shapes
- backend/app/core/db.py — database connection

## Notes
- The app seeds one example task on first run
- CORS is enabled for local frontends (React/Vite/etc.)
- Dates are in UTC
