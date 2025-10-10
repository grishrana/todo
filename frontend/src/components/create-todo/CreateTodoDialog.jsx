import React, { useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/create-todo/dialog";
import PriorityDropdown from "../ui/PriorityDropDown";
import { useTodo } from "@/hooks/useTodo";

export default function CreateTodoDialog() {
  const { createTask } = useTodo();
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState("");
  const [date, setDate] = useState("");
  const [priority, setPriority] = useState("medium");
  const [description, setDescription] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const isoDate = date ? new Date(date).toISOString() : "";
    console.log("task created..", { title, end_date: isoDate, priority, description });
    await createTask({
      title,
      end_date: isoDate,
      priority,
      description,
    });
    setTitle("");
    setDate("");
    setPriority("");
    setDescription("");
    setOpen(false);
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <div className="mx-auto w-48 h-12 bg-[#1e293b] flex items-center justify-center rounded-lg gap-2">
          <span className="text-2xl">Create Todo</span>
        </div>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[680px] min-h-[50%]">
        <form onSubmit={handleSubmit}>
          <DialogHeader>
            <DialogTitle>Task</DialogTitle>
          </DialogHeader>
          <div className="grid gap-3">
            <label htmlFor="title">Title</label>
            <input type="text" name="title" id="title" className="outline rounded-sm p-2"
              value={title} onChange={e => setTitle(e.target.value)} />
          </div>
          <div className="flex items-center gap-24">
            <div className="grid gap-2">
              <label htmlFor="date">Date</label>
              <input type="date" id="date" name="date" className="focus:outline-none"
                value={date} onChange={e => setDate(e.target.value)} />
            </div>
            <div className="grid gap-3">
              <label htmlFor="priority">Priority</label>
              <PriorityDropdown priority={priority} setPriority={setPriority} />
            </div>
          </div>
          <div className="grid gap-3">
            <label htmlFor="description">Description</label>
            <textarea name="description" id="description" rows={3} className="outline rounded-2xl p-4"
              value={description} onChange={e => setDescription(e.target.value)} />
          </div>
          <button type="submit" className="cursor-pointer">Add Task</button>
        </form>
      </DialogContent>
    </Dialog>
  );
}
