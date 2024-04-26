import unittest
import json
from datetime import datetime, timedelta

from todo-app import ToDoApp

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.todo_app = ToDoApp()

    def test_add_task(self):
        task_name = "Test Task"
        self.todo_app.add_task(task_name)
        self.assertGreater(len(self.todo_app.tasks), 0)
        self.assertIn(task_name, [task["name"] for task in self.todo_app.tasks])

    def test_view_tasks(self):
        task_name = "Test Task"
        self.todo_app.add_task(task_name)
        self.todo_app.view_tasks()
        self.assertGreater(len(self.todo_app.tasks), 0)
        self.assertIn(task_name, [task["name"] for task in self.todo_app.tasks])

    def test_mark_as_completed(self):
        task_name = "Test Task"
        self.todo_app.add_task(task_name)
        self.todo_app.mark_as_completed(0)  # Mark the first task as completed
        self.assertTrue(self.todo_app.tasks[0]["completed"])

    def test_remove_task(self):
        task_name = "Test Task"
        self.todo_app.add_task(task_name)
        self.todo_app.remove_task(0)  # Remove the first task
        self.assertLess(len(self.todo_app.tasks), 1)
        self.assertNotIn(task_name, [task["name"] for task in self.todo_app.tasks])

    def test_save_data(self):
        task_name = "Test Task"
        self.todo_app.add_task(task_name)
        self.todo_app.save_data()
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        self.assertGreater(len(tasks), 0)
        self.assertIn(task_name, [task["name"] for task in tasks])

    def test_load_data(self):
        tasks = [{"name": "Task 1", "due_date": datetime.now(), "completed": False}]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        self.todo_app.load_data()
        self.assertEqual(self.todo_app.tasks, tasks)

if __name__ == "__main__":
    unittest.main()
