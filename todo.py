import json
from datetime import datetime, timedelta

class ToDoApp:
    def __init__(self):
        self.tasks = []
        self.load_data()

    def display_menu(self):
        print("\n===== To-Do App Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

    def add_task(self):
        task_name = input("Enter task name: ")
        while True:
            due_date_str = input("Enter due date (YYYY-MM-DD HH:MM): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
            if due_date < datetime.now():
                print("Due date must be in the future.")
                return
            break

        self.tasks.append({"name": task_name, "due_date": due_date.strftime("%Y-%m-%d %H:%M"), "completed": False})
        print("Task added successfully!")
        self.save_data()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n===== Tasks =====")
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['name']} - Due: {task['due_date']} - Status: {status}")

    def mark_as_completed(self):
        self.view_tasks()

        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed!")
            self.save_data()
        else:
            print("Invalid task number. Please try again.")

    def remove_task(self):
        self.view_tasks()

        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(self.tasks):
            task_to_remove = self.tasks[task_index]
            self.tasks.remove(task_to_remove)
            print("Task removed successfully!")
            self.save_data()
        else:
            print("Invalid task number. Please try again.")

    def save_data(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_data(self):
        with open("tasks.json", "r") as file:
            self.tasks = json.load(file)

    def run(self):
        while True:
            self.display_menu()

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.mark_as_completed()
            elif choice == 4:
                self.remove_task()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
