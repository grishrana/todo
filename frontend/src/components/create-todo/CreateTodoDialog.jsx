import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/create-todo/dialog"
import PriorityDropdown from "../ui/PriorityDropDown";
import AddTask from "./AddTask";


export default function CreateTodoDialog() {
  
  const handleSubmit = (e) => {
    e.preventDefault();
  }
  
  return (
    <Dialog>
      <form onSubmit={handleSubmit}>
        <DialogTrigger asChild>
          <div className="mx-auto w-48 h-12 bg-[#1e293b] flex items-center justify-center rounded-lg gap-2">
            <span className="text-2xl">Create Todo</span>
          </div>
        </DialogTrigger>
        <DialogContent className="sm:max-w-[680px] min-h-[50%]">
          <DialogHeader>
            <DialogTitle>Task</DialogTitle>
          </DialogHeader>
          <div className="grid gap-3">
            <label htmlFor="title">Title</label>
            <input type="text" name="title" id="title" className="outline rounded-sm p-2" />
          </div>
          <div className="flex items-center gap-24">
            <div className="grid gap-2">
              <label htmlFor="date">Date</label>
              <input type="date" id="date" name="date" defaultValue className="focus:outline-none"/>
            </div>
            <div className="grid gap-3">
              <label htmlFor="date">Priority</label>
              <PriorityDropdown priority=""/> 
            </div>
          </div>
          <div className="grid gap-3">
            <label htmlFor="description">Description</label>
            <textarea name="description" id="description" rows={3} className="outline rounded-2xl p-4"></textarea>
          </div>
          <DialogFooter>
            <AddTask />
          </DialogFooter>
        </DialogContent>
      </form>
    </Dialog>
  )
}
