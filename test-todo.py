import unittest
import json
from datetime import datetime, timedelta
 import todo_app 

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.app = ToDoApp()

    def test_add_task(self):
        self.app.add_task("Test Task", datetime.now() + timedelta(days=1))
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0]["name"], "Test Task")
        self.assertEqual(self.app.tasks[0]["due_date"], (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"))
        self.assertFalse(self.app.tasks[0]["completed"])

    def test_view_tasks(self):
        self.app.add_task("Test Task 1", datetime.now() + timedelta(days=1))
        self.app.add_task("Test Task 2", datetime.now() + timedelta(days=2))
        self.app.view_tasks()
        self.assertEqual(len(self.app.tasks), 2)

    def test_mark_as_completed(self):
        self.app.add_task("Test Task 1", datetime.now() + timedelta(days=1))
        self.app.add_task("Test Task 2", datetime.now() + timedelta(days=2))
        self.app.mark_as_completed(1)
        self.assertTrue(self.app.tasks[0]["completed"])
        self.assertFalse(self.app.tasks[1]["completed"])

    def test_remove_task(self):
        self.app.add_task("Test Task 1", datetime.now() + timedelta(days=1))
        self.app.add_task("Test Task 2", datetime.now() + timedelta(days=2))
        self.app.remove_task(1)
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0]["name"], "Test Task 1")

    def test_save_data(self):
        self.app.add_task("Test Task 1", datetime.now() + timedelta(days=1))
        self.app.add_task("Test Task 2", datetime.now() + timedelta(days=2))
        self.app.save_data()
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["name"], "Test Task 1")
        self.assertEqual(tasks[0]["due_date"], (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"))
        self.assertFalse(tasks[0]["completed"])
        self.assertEqual(tasks[1]["name"], "Test Task 2")
        self.assertEqual(tasks[1]["due_date"], (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"))
        self.assertFalse(tasks[1]["completed"])

    def test_load_data(self):
        tasks = [
            {"name": "Test Task 1", "due_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"), "completed": False},
            {"name": "Test Task 2", "due_date": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"), "completed": False}
        ]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        self.app.load_data()
        self.assertEqual(len(self.app.tasks), 2)
        self.assertEqual(self.app.tasks[0]["name"], "Test Task 1")
        self.assertEqual(self.app.tasks[0]["due_date"], tasks[0]["due_date"])
        self.assertFalse(self.app.tasks[0]["completed"])
        self.assertEqual(self.app.tasks[1]["name"], "Test Task 2")
        self.assertEqual(self.app.tasks[1]["due_date"], tasks[1]["due_date"])
        self.assertFalse(self.app.tasks[1]["completed"])

if __name__ == "__main__":
    unittest.main()
