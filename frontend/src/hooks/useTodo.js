import { useContext } from "react";
import { TodoContext } from "../context";

export const useTodo = () => useContext(TodoContext);