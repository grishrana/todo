import { useState } from "react";
import dropdownIcon from "../../assets/dropdown-icon.svg";
import wrapupIcon from "../../assets/wrapup-icon.svg";

function PriorityDropdown({priority, setPriority}) {
  const [isOpen, setIsOpen] = useState(false);

  const priorities = ["high", "medium", "low"];

  const handleSelect = (priority) => {
    setPriority(priority);
    setIsOpen(false);
  };

  return (
    <div className="">
      <button
        id="priority"
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center justify-center"
      >
        {priority ? priority : "medium"}
        <img src={isOpen? wrapupIcon: dropdownIcon}
         alt="dropdown" />
      </button>

      {isOpen && (
        <ul className="absolute mt-2 w-40 rounded-md shadow-lg ring-1 ring-black ring-opacity-5">
          {priorities.map((priority) => (
            <li
              key={priority}
              className="block px-4 py-2 cursor-pointer hover:bg-gray-600 hover:text-gray-100"
              onClick={() => handleSelect(priority)}
            >
              {priority}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default PriorityDropdown;
