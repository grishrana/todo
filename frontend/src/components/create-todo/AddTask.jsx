import { useTodo } from "@/hooks/useTodo";

function AddTask() {
  const { createTask } = useTodo();
  
  return (
    <div className="mx-auto w-48 h-12 bg-[#1e293b] flex items-center justify-center rounded-lg gap-2">
        <button className="text-2xl" onClick={createTask}>Add Task</button>
    </div>
  );
}

export default AddTask;
