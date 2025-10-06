import { data } from "@/context/todos";
import { createContext, useContext } from "react";

export const TodoContext = createContext({
    todos: data,
    showTasks: ()=> {},
    showTask: ()=> {},
    createTask: ()=> {},
    updateTask: ()=> {},
    deleteTask: ()=> {}
});

export const useTodo = () => {
    return useContext(TodoContext);
}

export const TodoContextProvider = TodoContext.Provider;