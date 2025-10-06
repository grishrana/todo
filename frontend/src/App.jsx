import TodoItems from "./components/TodoItems"
import CreateTodoDialog from "./components/create-todo/CreateTodoDialog"
import { TodoContextProvider, useTodo } from "./context/TodoContext"
import ShowTodo from "./components/ui/ShowTodo"
import CreateTodo from "./components/create-todo/AddTask"
import UpdateTodo from "./components/update-todo/UpdateTaskIcon"
import DeleteTodo from "./components/ui/DeleteTodo"

function App() {
  const { todos } = useTodo();

  return (
    <TodoContextProvider value={{todos, ShowTodo, CreateTodo, UpdateTodo, DeleteTodo}}>
      <div className="p-2">
        <TodoItems data={todos} />
        <CreateTodoDialog />
      </div>
    </TodoContextProvider>
  )}

export default App
