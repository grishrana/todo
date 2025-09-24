# Running the project

## 1) Install tools

- Python 3.11+
- PostgreSQL

## 2) Install Python packages

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn sqlmodel psycopg[binary] python-dotenv
```

## 3) Prepare database

- Create a database named `smart_todo`:

```bash
createdb smart_todo
```

- Set env vars in a `.env` file:

```bash
DB_USER=your_db_user
DB_PASS=your_db_password
```

## 4) Run the server

```bash
uvicorn backend.app.main:app --reload
```

Open in browser:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## 5) Try it out

List tasks:

```bash
curl http://127.0.0.1:8000/api/v1/show
```

Create a task:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/create \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Watch a tutorial",
    "priority": "medium",
    "end_date": "2025-10-25T00:00:00Z"
  }'
```

