import React from "react";
import checkedIcon from "../../assets/checked-icon.svg";
import uncheckedIcon from "../../assets/unchecked-icon.svg";
import DeleteTodo from "./DeleteTodo";
import ShowTodo from "./ShowTodo";
import UpdateTodoDialog from "../update-todo/UpdateTodoDialog";

function TodoItem({ todo }) {
  return (
    <div className="w-[90%] h-auto m-8 p-4 bg-[#1e293b] rounded-2xl flex items-center justify-between">
      <div className="flex items-center gap-4">
        {todo.completed ? (
          <>
            <img src={checkedIcon} alt="checked item" className="cursor-pointer hover:scale-111 w-8" />
            <div className="text-xl line-through">{todo.title}</div>
          </>
        ) : (
          <>
            <img src={uncheckedIcon} alt="unchecked item" className="cursor-pointer hover:scale-111 w-8" />
            <div className="text-xl">{todo.title}</div>
          </>
        )}
      </div>
      
      <div className="flex items-center justify-between gap-5">
        <UpdateTodoDialog todo={todo}/>
        <DeleteTodo todo={todo}/>
        <ShowTodo todo={todo}/>
      </div>
    </div>
  );
}

export default TodoItem;