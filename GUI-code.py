import tkinter as tk
from tkinter import messagebox

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
listbox.trace_add("w", lambda *args: update_task_counts())
listbox_completed.trace_add("w", lambda *args: update_task_counts())

# Start the main loop
app.mainloop()

