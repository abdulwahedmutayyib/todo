import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_as_completed():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        listbox.delete(selected_task)
        listbox_completed.insert(tk.END, task)
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def clear_completed_tasks():
    listbox_completed.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("To-Do List App")

# Create the task entry and buttons
entry = tk.Entry(app, width=40)
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
completed_button = tk.Button(app, text="Mark as Completed", command=mark_as_completed)
clear_button = tk.Button(app, text="Clear Completed", command=clear_completed_tasks)

# Create the task listbox
listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
listbox_completed = tk.Listbox(app, selectmode=tk.SINGLE, height=5, width=40)

# Label to display task counts
task_count_label = tk.Label(app, text="Total Tasks: 0")
completed_count_label = tk.Label(app, text="Completed Tasks: 0")

# Place widgets in the window
entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
completed_button.pack(pady=5)
clear_button.pack(pady=5)
listbox.pack(pady=10)
listbox_completed.pack(pady=10)
task_count_label.pack()
completed_count_label.pack()

# Update task counts
def update_task_counts():
    total_tasks = listbox.size()
    completed_tasks = listbox_completed.size()
    task_count_label.config(text=f"Total Tasks: {total_tasks}")
    completed_count_label.config(text=f"Completed Tasks: {completed_tasks}")

# Set up a trace on listbox to update counts when it changes
listbox.trace_add("w", lambda *args: update_task_counts())
listbox_completed.trace_add("w", lambda *args: update_task_counts())

# Start the main loop
app.mainloop()



