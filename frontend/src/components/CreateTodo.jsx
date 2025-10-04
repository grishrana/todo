
const handleClick = () => {
    
}

function CreateTodo() {
  return (
    <div className="mx-auto w-48 h-12 bg-[#1e293b] flex items-center justify-center rounded-lg gap-2">
        <button className="text-2xl" onClick={handleClick}>Create Todo</button>
    </div>
  );
}

export default CreateTodo;
