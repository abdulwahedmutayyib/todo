import json
from datetime import datetime, timedelta

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n===== To-Do App Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

    def add_task(self):
        task_name = input("Enter task name: ")
        due_date_str = input("Enter due date (YYYY-MM-DD HH:MM): ")

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
            return

        self.tasks.append({"name": task_name, "due_date": due_date, "completed": False})
        print("Task added successfully!")

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

        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def remove_task(self):
        self.view_tasks()

        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(self.tasks):
                del self.tasks[task_index]
                print("Task removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def save_data(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_data(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def run(self):
        self.load_data()

        while True:
            self.display_menu()

            try:
                choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.mark_as_completed()
            elif choice == 4:
                self.remove_task()
            elif choice == 5:
                self.save_data()
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_app = ToDoApp()
    todo_app.run()
