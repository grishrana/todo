import dropdownIcon from "../../assets/dropdown-icon.svg";

const handleClick = () => {
    
}

function ShowTodo() {
  return (
    <button onClick={handleClick}>
        <img src={dropdownIcon} alt="showtodo" />
    </button>
  );
}

export default ShowTodo;
