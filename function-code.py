import os

TODO_FILE = "todo.txt"
COMPLETED_FILE = "completed.txt"

def initialize_files():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w"):
            pass

    if not os.path.exists(COMPLETED_FILE):
        with open(COMPLETED_FILE, "w"):
            pass

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")

def list_tasks():
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
        if tasks:
            print("To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
        else:
            print("No tasks in the To-Do list.")

def mark_as_completed(task_index):
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()

    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)

        with open(COMPLETED_FILE, "a") as file:
            file.write(completed_task)

        print(f"Marked task as completed: {completed_task.strip()}")
    else:
        print("Invalid task index.")

def clear_completed_tasks():
    with open(COMPLETED_FILE, "w"):
        pass
    print("Cleared completed tasks.")

def main():
    initialize_files()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            list_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_as_completed(task_index)

        elif choice == "4":
            clear_completed_tasks()

        elif choice == "5":
            print("Exiting To-Do App.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
