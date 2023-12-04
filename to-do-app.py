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

# Create the main window
app = tk.Tk()
app.title("To-Do List App")

# Create the task entry and buttons
entry = tk.Entry(app, width=40)
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)

# Create the task listbox
listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)

# Place widgets in the window
entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
listbox.pack(pady=10)

# Start the main loop
app.mainloop()

