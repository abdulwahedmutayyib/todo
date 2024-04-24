import unittest
import json
from datetime import datetime, timedelta

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.todo_app = ToDoApp()

    def test_add_task(self):
        self.todo_app.add_task()
        self.assertGreater(len(self.todo_app.tasks), 0)

    def test_view_tasks(self):
        self.todo_app.add_task()
        self.todo_app.view_tasks()
        self.assertGreater(len(self.todo_app.tasks), 0)

    def test_mark_as_completed(self):
        self.todo_app.add_task()
        self.todo_app.mark_as_completed()
        self.assertTrue(self.todo_app.tasks[0]["completed"])

    def test_remove_task(self):
        self.todo_app.add_task()
        self.todo_app.remove_task()
        self.assertLess(len(self.todo_app.tasks), 1)

    def test_save_data(self):
        self.todo_app.add_task()
        self.todo_app.save_data()
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        self.assertGreater(len(tasks), 0)

    def test_load_data(self):
        tasks = [{"name": "Task 1", "due_date": datetime.now(), "completed": False}]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        self.todo_app = ToDoApp()
        self.todo_app.load_data()
        self.assertEqual(self.todo_app.tasks, tasks)

if __name__ == "__main__":
    unittest.main()
