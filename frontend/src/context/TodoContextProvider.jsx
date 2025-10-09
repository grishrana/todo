import { createTodo, deleteTodo, fetchTodos, updateTodo } from "@/lib/todoApi";
import { useState } from "react";
import { createContext } from "react";
import { data } from "./todos";

const TodoContext = createContext();

function TodoContextProvider({children}) {
    const [todos, setTodos] = useState(data);
    
    async function showTasks() {
        const data=await fetchTodos();
        setTodos(data);
    }
    
    function showTask(id) {
        return todos.find((t)=>t.id===id);
    }
    
    async function createTask(task) {
        await createTodo(task);
        await showTasks();
    }
    
    async function updateTask(id, task) {
        await updateTodo(id, task);
        await showTasks();
    }
    
    async function deleteTask(id) {
        await deleteTodo(id);
        await showTasks();
    }
    
    return (
        <TodoContext.Provider value={{todos, showTasks, showTask, createTask, updateTask, deleteTask}}>
            {children}
        </TodoContext.Provider>
    )
}

export { TodoContext, TodoContextProvider };
export default TodoContextProvider;