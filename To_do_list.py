import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    description = entry_description.get()
    if description:
        tasks = load_tasks()
        task_id = len(tasks) + 1
        tasks.append({'id': task_id, 'description': description, 'completed': False})
        save_tasks(tasks)
        list_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task description")

def list_tasks():
    for widget in frame_tasks.winfo_children():
        widget.destroy()
    tasks = load_tasks()
    for task in tasks:
        status = 'Completed' if task['completed'] else 'Pending'
        tk.Label(frame_tasks, text=f"ID: {task['id']} | Description: {task['description']} | Status: {status}").pack()

root = tk.Tk()
root.title("To-Do List")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)
entry_description = tk.Entry(frame_input, width=50)
entry_description.pack(side=tk.LEFT)
button_add = tk.Button(frame_input, text="Add Task", command=add_task)
button_add.pack(side=tk.LEFT)

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

list_tasks()

root.mainloop()
