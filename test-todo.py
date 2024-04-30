import unittest
from todo_app import ToDoApp  # assuming the code is in a file called todo_app.py

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.app = ToDoApp()

    def test_add_task(self):
        self.app.add_task()
        self.assertEqual(len(self.app.tasks), 1)

    def test_view_tasks(self):
        self.app.add_task()
        self.app.add_task()
        self.app.view_tasks()
        self.assertEqual(len(self.app.tasks), 2)

    def test_mark_as_completed(self):
        self.app.add_task()
        self.app.mark_as_completed()
        self.assertTrue(self.app.tasks[0]["completed"])

    def test_remove_task(self):
        self.app.add_task()
        self.app.add_task()
        self.app.remove_task()
        self.assertEqual(len(self.app.tasks), 1)

    def test_save_data(self):
        self.app.add_task()
        self.app.save_data()
        with open("tasks.json", "r") as file:
            data = json.load(file)
        self.assertEqual(len(data), 1)

    def test_load_data(self):
        with open("tasks.json", "w") as file:
            json.dump([{"name": "Task 1", "due_date": "2023-03-01 12:00", "completed": False}], file)
        self.app.load_data()
        self.assertEqual(len(self.app.tasks), 1)

if __name__ == "__main__":
    unittest.main()
