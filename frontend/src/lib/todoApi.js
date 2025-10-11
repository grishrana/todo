import axios from "axios";

// const API_BASE="http://127.0.0.1:8000/api/v1";
const API_BASE="http://127.0.0.1:8000/api/v1/api/v1";

export async function fetchTodos() {
    const res = await axios.get(`${API_BASE}/show`);
    console.log(res.data);
    return res.data.data || res.data;
}

export async function createTodo(todo) {
    await axios.post(`${API_BASE}/create`, todo);
}

export async function updateTodo(id, todo) {
    await axios.put(`${API_BASE}/update/${id}`, todo);
}

export async function deleteTodo(id) {
    await axios.delete(`${API_BASE}/delete/${id}`);
}