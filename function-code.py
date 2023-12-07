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

def update_task_counts():
    total_tasks = listbox.size()
    completed_tasks = listbox_completed.size()
    task_count_label.config(text=f"Total Tasks: {total_tasks}")
    completed_count_label.config(text=f"Completed Tasks: {completed_tasks}")

