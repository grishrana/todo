import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/create-todo/dialog";
import UpdateTaskIcon from "./UpdateTaskIcon";
import PriorityDropdown from "../ui/PriorityDropDown";

export default function UpdateTodoDialog({todo}) {
  
  const handleSubmit = (e) => {
    e.preventDefault();
  }
  
  return (
    <Dialog>
      <form onSubmit={handleSubmit}>
        <DialogTrigger asChild>
          {/* <span>{todo.id}</span> */}
          <UpdateTaskIcon />
        </DialogTrigger>
        <DialogContent className="sm:max-w-[680px] min-h-[50%]">
          <DialogHeader>
            <DialogTitle>Task</DialogTitle>
          </DialogHeader>
          <div className="grid gap-3">
            <label htmlFor="title">Title</label>
            <input type="text" defaultValue={todo.title} name="title" id="title" className="outline rounded-sm p-2" />
          </div>
          <div className="flex items-center gap-24">
            <div className="grid gap-2">
              <label htmlFor="date">Date</label>
              <input
                type="date"
                defaultValue={todo.end_date.split("T")[0]}
                id="date" name="date" className="focus:outline-none"
                />
            </div>
            <div className="grid gap-3">
              <label htmlFor="date">Priority</label>
              <PriorityDropdown priority={todo.priority}/> 
            </div>
          </div>
          <div className="grid gap-3">
            <label htmlFor="description">Description</label>
            <textarea name="description" value={todo.description} id="description" rows={3} className="outline rounded-2xl p-4"></textarea>
          </div>
          <DialogFooter>
            <button type="submit">Update Task</button>
          </DialogFooter>
        </DialogContent>
      </form>
    </Dialog>
  )
}
