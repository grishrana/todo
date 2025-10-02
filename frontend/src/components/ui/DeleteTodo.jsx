import deleteIcon from "../../assets/delete-icon.svg";

const handleClick = () => {
  
}

function DeleteTodo({todo}) {
  return(
    <button onClick={handleClick}>
      <img src={deleteIcon} alt="delete" />
    </button>
  );
}

export default DeleteTodo;
