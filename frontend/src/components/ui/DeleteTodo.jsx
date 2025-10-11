import { useTodo } from "@/hooks/useTodo";
import deleteIcon from "../../assets/delete-icon.svg";

function DeleteTodo({todo}) {
  const { deleteTask } = useTodo();
  
  return(
    <button onClick={()=> deleteTask(todo.id)} className="cursor-pointer hover:bg-[#0f172a] hover:rounded-lg hover:scale-111">
      <img src={deleteIcon} alt="delete" className="w-10"/>
    </button>
  );
}

export default DeleteTodo;
