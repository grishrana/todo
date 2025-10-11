import TodoItems from "./components/TodoItems"
import CreateTodoDialog from "./components/create-todo/CreateTodoDialog"
import ShowTodo from "./components/ui/ShowTodo"
import { useTodo } from "./hooks/useTodo"
import TodoContextProvider from "./context/TodoContextProvider"

function AppContent() {
  const {todos} = useTodo();
  return (
    <div className="p-2">
      <TodoItems data={todos} />
      <CreateTodoDialog />
    </div>
  );
}

function App() {
  return (
    <TodoContextProvider>
      <AppContent />
    </TodoContextProvider>
  )}

export default App
