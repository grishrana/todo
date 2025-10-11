import React from "react";
import TodoItem from "./ui/TodoItem";

function TodoItems({data}) {
  return (
    <div>
        {data.map((todo)=>(
            <TodoItem key={todo.id} todo={todo} />
        ))}
    </div>
  )
}

export default TodoItems;
