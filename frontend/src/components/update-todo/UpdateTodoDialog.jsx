import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/create-todo/dialog";
import UpdateTaskIcon from "./UpdateTaskIcon";
import PriorityDropdown from "../ui/PriorityDropDown";
import { useState } from "react";
import { useTodo } from "@/hooks/useTodo";

export default function UpdateTodoDialog({todo}) {
  const { updateTask } = useTodo();
  const id = todo.id;
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState(todo.title);
  const [date, setDate] = useState(todo.end_date);
  const [priority, setPriority] = useState(todo.priority);
  const [description, setDescription] = useState(todo.description);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const isoDate = date ? new Date(date).toISOString() : "";
     console.log("task updated..", { title, end_date: isoDate, priority, description });
    await updateTask(
      id, {
        title,
        end_date: isoDate,
        priority,
        description,
      }
    );
    setOpen(false);
  }
  
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <UpdateTaskIcon />
      </DialogTrigger>
      <DialogContent className="sm:max-w-[680px] min-h-[50%]">
        <form onSubmit={handleSubmit}>
          <DialogHeader>
            <DialogTitle>Task</DialogTitle>
          </DialogHeader>
          <div className="grid gap-3">
            <label htmlFor="title">Title</label>
            <input type="text" defaultValue={title} onChange={(e)=>setTitle(e.target.value)} name="title" id="title" className="outline rounded-sm p-2" />
          </div>
          <div className="flex items-center gap-24">
            <div className="grid gap-2">
              <label htmlFor="date">Date</label>
              <input
                type="date"
                defaultValue={date.split(['T'])[0]}
                onChange={(e)=>setDate(e.target.value)}
                id="date" name="date" className="focus:outline-none"
                />
            </div>
            <div className="grid gap-3">
              <label htmlFor="date">Priority</label>
              <PriorityDropdown priority={priority} setPriority={setPriority}/> 
            </div>
          </div>
          <div className="grid gap-3">
            <label htmlFor="description">Description</label>
            <textarea name="description" value={description} onChange={(e)=>setDescription(e.target.value)} id="description" rows={3} className="outline rounded-2xl p-4"></textarea>
          </div>
          <button type="submit">Update Task</button>
        </form>
      </DialogContent>
    </Dialog>
  )
}
