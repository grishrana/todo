
# Todo Frontend

A simple React frontend for the Todo app. This UI lets you create, view, update, and delete todo tasks, connecting to a FastAPI backend.

## Features
- View a list of todos
- Create a new todo (with title, description, date, and priority)
- Edit and update existing todos
- Delete todos
- Expand to see todo details

## Getting Started

Clone the repo and start the frontend server:

```sh
cd frontend
npm install
npm run dev
```

The app will be available at [http://localhost:5173](http://localhost:5173) by default.

## Project Structure & Responsibilities

- **API Calls:**
	- All API requests to the backend are handled in [`src/lib/todoApi.js`](src/lib/todoApi.js).
	- This file contains functions for fetching, creating, updating, and deleting todos.

- **Context & State Management:**
	- The todo context and all related logic are defined in [`src/context`](src/context).
	- The context provides todos and CRUD functions to all components.

- **Creating Todos:**
	- The dialog and form for creating a new todo are in [`src/components/create-todo`](src/components/create-todo).
	- This includes the form fields, and logic to submit a new todo.

- **Updating Todos:**
	- The dialog and form for editing/updating a todo are in [`src/components/update-todo`](src/components/update-todo).

- **UI Components:**
	- Lower-level, reusable UI components (like buttons, dropdowns, and todo item display) are in [`src/components/ui`](src/components/ui).

- **Hooks:**
	- Custom hooks (like `useTodo`) are in [`src/hooks`](src/hooks).

## Notes
- The UI is intentionally simple and minimal.
- Make sure your backend server is running and accessible for API calls to work.

---