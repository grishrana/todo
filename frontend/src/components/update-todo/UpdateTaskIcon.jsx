import React from "react";
import editIcon from "../../assets/edit-icon.svg";

const UpdateTaskIcon = React.forwardRef((props, ref)=> {
  return (
    <button ref={ref} className="cursor-pointer hover:bg-[#0f172a] hover:rounded-lg hover:scale-111" {...props}>
      <img src={editIcon} alt="edit" className="w-10"/>
    </button>
  )
})

export default UpdateTaskIcon;