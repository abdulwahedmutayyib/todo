import unittest
from unittest.mock import patch, MagicMock
from todo import ToDoApp  # assuming the code is in a file called todo_app.py

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.app = ToDoApp()

    def test_display_menu(self):
        with patch('builtins.print') as mock_print:
            self.app.display_menu()
            mock_print.assert_called_with("\n===== To-Do App Menu =====")
            mock_print.assert_called_with("1. Add Task")
            mock_print.assert_called_with("2. View Tasks")
            mock_print.assert_called_with("3. Mark Task as Completed")
            mock_print.assert_called_with("4. Remove Task")
            mock_print.assert_called_with("5. Exit")

    def test_add_task(self):
        with patch('builtins.input', side_effect=["Task 1", "2022-01-01 12:00"]):
            self.app.add_task()
            self.assertEqual(len(self.app.tasks), 1)
            self.assertEqual(self.app.tasks[0]["name"], "Task 1")
            self.assertEqual(self.app.tasks[0]["due_date"], "2022-01-01 12:00")
            self.assertFalse(self.app.tasks[0]["completed"])

    def test_view_tasks(self):
        self.app.tasks = [{"name": "Task 1", "due_date": "2022-01-01 12:00", "completed": False}]
        with patch('builtins.print') as mock_print:
            self.app.view_tasks()
            mock_print.assert_called_with("\n===== Tasks =====")
            mock_print.assert_called_with("1. Task 1 - Due: 2022-01-01 12:00 - Status: Pending")

    def test_mark_as_completed(self):
        self.app.tasks = [{"name": "Task 1", "due_date": "2022-01-01 12:00", "completed": False}]
        with patch('builtins.input', return_value="1"):
            self.app.mark_as_completed()
            self.assertTrue(self.app.tasks[0]["completed"])

    def test_remove_task(self):
        self.app.tasks = [{"name": "Task 1", "due_date": "2022-01-01 12:00", "completed": False}]
        with patch('builtins.input', return_value="1"):
            self.app.remove_task()
            self.assertEqual(len(self.app.tasks), 0)

    def test_save_data(self):
        self.app.tasks = [{"name": "Task 1", "due_date": "2022-01-01 12:00", "completed": False}]
        with patch('json.dump') as mock_dump:
            self.app.save_data()
            mock_dump.assert_called_once_with(self.app.tasks, MagicMock())

    def test_load_data(self):
        with patch('json.load', return_value=[{"name": "Task 1", "due_date": "2022-01-01 12:00", "completed": False}]):
            self.app.load_data()
            self.assertEqual(len(self.app.tasks), 1)
            self.assertEqual(self.app.tasks[0]["name"], "Task 1")
            self.assertEqual(self.app.tasks[0]["due_date"], "2022-01-01 12:00")
            self.assertFalse(self.app.tasks[0]["completed"])

if __name__ == "__main__":
    unittest.main()
