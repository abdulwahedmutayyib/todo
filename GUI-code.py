import tkinter as tk
from tkinter import messagebox

TODO_FILE = "todo.txt"
COMPLETED_FILE = "completed.txt"

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")

        self.initialize_files()

        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.list_button = tk.Button(master, text="List Tasks", command=self.list_tasks)
        self.list_button.pack(pady=5)

        self.mark_button = tk.Button(master, text="Mark as Completed", command=self.mark_as_completed)
        self.mark_button.pack(pady=5)

        self.clear_button = tk.Button(master, text="Clear Completed", command=self.clear_completed_tasks)
        self.clear_button.pack(pady=5)

    def initialize_files(self):
        if not tk.StringVar(TODO_FILE).get():
            with open(TODO_FILE, "w"):
                pass

        if not tk.StringVar(COMPLETED_FILE).get():
            with open(COMPLETED_FILE, "w"):
                pass

    def add_task(self):
        task = self.entry.get()
        if task:
            with open(TODO_FILE, "a") as file:
                file.write(task + "\n")
            messagebox.showinfo("Success", "Task added successfully.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def list_tasks(self):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            if tasks:
                task_list = "\n".join(tasks)
                messagebox.showinfo("To-Do List", f"To-Do List:\n{task_list}")
            else:
                messagebox.showinfo("To-Do List", "No tasks in the To-Do list.")

    def mark_as_completed(self):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()

        if tasks:
            selected_task = messagebox.askinteger("Mark as Completed", "Enter the index of the task to mark as completed:")
            if selected_task and 1 <= selected_task <= len(tasks):
                completed_task = tasks.pop(selected_task - 1)
                with open(TODO_FILE, "w") as file:
                    file.writelines(tasks)

                with open(COMPLETED_FILE, "a") as file:
                    file.write(completed_task)
                messagebox.showinfo("Success", f"Marked task as completed: {completed_task.strip()}")
            else:
                messagebox.showwarning("Warning", "Invalid task index.")
        else:
            messagebox.showinfo("To-Do List", "No tasks in the To-Do list.")

    def clear_completed_tasks(self):
        with open(COMPLETED_FILE, "w"):
            pass
        messagebox.showinfo("Success", "Cleared completed tasks.")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
