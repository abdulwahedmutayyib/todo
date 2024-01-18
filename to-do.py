import datetime
import time
from win10toast import ToastNotifier
import pyttsx3
import json
import os

class TodoList:
    def __init__(self, username):
        self.tasks = []
        self.toaster = ToastNotifier()
        self.engine = pyttsx3.init()
        self.voice_reminders_enabled = False
        self.username = username
        self.load_tasks()

    def add_task(self, task, due_date=None):
        if due_date:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d %H:%M")
            self.schedule_reminder(task, due_date)

        self.tasks.append({"task": task, "due_date": due_date, "created_at": datetime.datetime.now()})
        self.save_tasks()
        print(f'\033[95mTask "{task}" added successfully.\033[0m')

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                self.save_tasks()
                print(f'\033[95mTask "{task}" removed successfully.\033[0m')
                return
        print(f'\033[91mTask "{task}" not found in the list.\033[0m')

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed_at"] = datetime.datetime.now()
                self.save_tasks()
                print(f'\033[95mTask "{task}" marked as completed.\033[0m')
                return
        print(f'\033[91mTask "{task}" not found in the list.\033[0m')

    def show_tasks(self, show_completed=False):
        if not self.tasks:
            print('\033[93mNo tasks in the list.\033[0m')
        else:
            print('\033[94mTasks:\033[0m')
            for i, task in enumerate(self.tasks, start=1):
                completed_status = "Completed" if "completed_at" in task else "Not Completed"
                created_at = task["created_at"].strftime("%Y-%m-%d %H:%M:%S")
                due_date = task.get("due_date", None)
                completed_at = task.get("completed_at", None)

                if show_completed or not completed_at:
                    task_info = f'{i}. {task["task"]} (\033[92m{completed_status}\033[0m) - Created at: {created_at}'
                    if due_date:
                        task_info += f', Due Date: {due_date.strftime("%Y-%m-%d %H:%M")}'
                    print(task_info)

    def toggle_voice_reminders(self):
        self.voice_reminders_enabled = not self.voice_reminders_enabled
        status = "enabled" if self.voice_reminders_enabled else "disabled"
        print(f'\033[94mVoice reminders are now {status}.\033[0m')

    def schedule_reminder(self, task, due_date):
        if self.voice_reminders_enabled:
            reminder_time = due_date - datetime.timedelta(hours=1)
            current_time = datetime.datetime.now()

            if reminder_time > current_time:
                time_diff = (reminder_time - current_time).seconds
                time.sleep(time_diff)
                self.show_reminder_notification(task)
                self.speak_reminder(task)

    def show_reminder_notification(self, task):
        self.toaster.show_toast("Task Reminder", f'One hour left for the task: "{task}"', duration=10)

    def speak_reminder(self, task):
        self.engine.say(f"One hour left for the task: {task}")
        self.engine.runAndWait()

    def save_tasks(self):
        data = {
            "username": self.username,
            "tasks": self.tasks,
            "voice_reminders_enabled": self.voice_reminders_enabled
        }

        with open(f"{self.username}_tasks.json", "w") as file:
            json.dump(data, file)

    def load_tasks(self):
        filename = f"{self.username}_tasks.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = data.get("tasks", [])
                self.voice_reminders_enabled = data.get("voice_reminders_enabled", False)

def login():
    username = input("\033[94mEnter your username: \033[0m")
    password = input("\033[94mEnter your password: \033[0m")  # In a real application, use secure password storage methods
    return username

def main():
    username = login()
    todo_list = TodoList(username)

    while True:
        print("\n\033[94mOptions:\033[0m")
        print("\033[94m1. Add Task\033[0m")
        print("\033[94m2. Remove Task\033[0m")
        print("\033[94m3. Complete Task\033[0m")
        print("\033[94m4. Show Tasks\033[0m")
        print("\033[94m5. Show Completed Tasks\033[0m")
        print("\033[94m6. Toggle Voice Reminders\033[0m")
        print("\033[94m7. Quit\033[0m")

        choice = input("\033[94mEnter your choice (1-7): \033[0m")

        if choice == '1':
            task = input("\033[94mEnter the task: \033[0m")
            due_date_str = input("\033[94mEnter the due date (YYYY-MM-DD HH:MM), if any (press Enter to skip): \033[0m")
            todo_list.add_task(task, due_date_str)
        elif choice == '2':
            task = input("\033[94mEnter the task to remove: \033[0m")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("\033[94mEnter the task to mark as completed: \033[0m")
            todo_list.complete_task(task)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            todo_list.show_tasks(show_completed=True)
        elif choice == '6':
            todo_list.toggle_voice_reminders()
        elif choice == '7':
            print("\033[94mExiting the to-do list app. Goodbye!\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please enter a number between 1 and 7.\033[0m")

if __name__ == "__main__":
    main()
