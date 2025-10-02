import editIcon from "../../assets/edit-icon.svg";

const handleClick = () => {
    
}

function EditTodo() {
  return (
    <button onClick={handleClick}>
        <img src={editIcon} alt="edittodo" />
    </button>
  );
}

export default EditTodo;
