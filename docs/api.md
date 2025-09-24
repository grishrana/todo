# API Overview

Base URL (local): <http://127.0.0.1:8000>

Interactive docs are available when the server is running:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

Note: The app uses a root path and also prefixes routes with `/api/v1`. Use the paths below as shown.

## Endpoints

### GET /

Returns a hello message.

Response:

```json
{
  "data": "Hello World"
}
```

### GET /api/v1/show

List all tasks.

Response (200):

```json
{
  "data": [
    {
      "id": 1,
      "title": "Develop Smart Todo",
      "description": "...",
      "priority": "medium",
      "created_at": "2025-10-01T00:00:00Z",
      "end_date": "2025-10-25T00:00:00Z",
      "completed": false
    }
  ]
}
```

### GET /api/v1/{id}

Get one task by id.

- Path params: `id` (integer)
- Errors: 404 if not found

### POST /api/v1/create

Create a new task.

Body example:

```json
{
  "title": "Learn FastAPI",
  "description": "Watch a tutorial",
  "priority": "medium",
  "end_date": "2025-10-25T00:00:00Z"
}
```

Response (201):

```json
{
  "data": {
    "id": 2,
    "title": "Learn FastAPI",
    "description": "Watch a tutorial",
    "priority": "medium",
    "created_at": "2025-09-23T12:00:00Z",
    "end_date": "2025-10-25T00:00:00Z",
    "completed": false
  }
}
```

### PUT /api/v1/update/{id}

Update a task.

Body example:

```json
{
  "title": "Learn FastAPI (updated)",
  "description": "Read docs",
  "priority": "high",
  "end_date": "2025-10-26T00:00:00Z",
  "completed": true
}
```

### DELETE /api/v1/delete/{id}

Delete a task.

- Response status: 204 (no body)

## Data types

- `priority`: one of `high`, `medium`, `low`
- `end_date` and `created_at`: ISO 8601 DateTime in UTC (example: `2025-10-25T00:00:00Z`)

