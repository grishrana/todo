import React from "react";
import checkedIcon from "../../assets/checked-icon.svg";
import uncheckedIcon from "../../assets/unchecked-icon.svg";

function TodoItem({ todo }) {
  return (
    <div className="w-full p-4 h-auto m-4 bg-[#1e293b] ">
      {todo.completed ? (
        <img src={checkedIcon} alt="checked item" />
      ) : (
        <img src={uncheckedIcon} alt="unchecked item" />
      )}
      <div></div>
      <div>
        <EditTodo todo={todo}/>
        <DeleteTodo todo={todo}/>
        <ShowTodo todo={todo}/>
      </div>
    </div>
  );
}

export default TodoItem;