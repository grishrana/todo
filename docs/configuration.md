# Configuration

## Environment variables

Create a file named `.env` in the project root with:

```bash
DB_USER=your_db_user
DB_PASS=your_db_password
```

## Database

- PostgreSQL is used.
- The app connects to `postgresql://DB_USER:DB_PASS@localhost:5432/smart_todo`.
- Make sure a database named `smart_todo` exists:

```bash
createdb smart_todo
```

## Seeding

On first run, the app creates tables and inserts one example task automatically.

## CORS (browsers)

Allowed local addresses are set in the app:

- `http://localhost:8080`
- `http://localhost:5173`
- `http://localhost:3000`

You can change these in `backend/app/main.py`.

