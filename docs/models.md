# Data models

## Task
Fields:
- `id` (int): primary key
- `title` (string): short name of the task
- `description` (string | null): optional details
- `priority` (string): one of `high`, `medium`, `low` (default: `medium`)
- `created_at` (datetime): set automatically when the task is created (UTC)
- `end_date` (datetime): when the task should be done (UTC)
- `completed` (bool): whether the task is done (default: false)

## PriorityEnum
- `high`
- `medium`
- `low`

## Notes
- Dates are ISO 8601 in UTC (example: `2025-10-25T00:00:00Z`).
- A `user` table exists in code as a placeholder and may be linked later.