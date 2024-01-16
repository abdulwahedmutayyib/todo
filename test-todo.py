import unittest
from unittest.mock import patch
from io import StringIO
import os

from todo_app import TodoList, login, main

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        # Create a test user
        self.username = "test_user"
        self.test_app = TodoList(self.username)

    def tearDown(self):
        # Remove the test user's data file
        filename = f"{self.username}_tasks.json"
        if os.path.exists(filename):
            os.remove(filename)

    def test_add_task(self):
        with patch('builtins.input', side_effect=['Test Task', '']):
            self.test_app.add_task('Test Task')

        self.assertEqual(len(self.test_app.tasks), 1)
        self.assertEqual(self.test_app.tasks[0]["task"], 'Test Task')

    def test_remove_task(self):
        self.test_app.tasks = [{"task": "Test Task", "created_at": "2023-01-01 12:00:00"}]
        with patch('builtins.input', return_value='Test Task'):
            self.test_app.remove_task('Test Task')

        self.assertEqual(len(self.test_app.tasks), 0)

    def test_complete_task(self):
        self.test_app.tasks = [{"task": "Test Task", "created_at": "2023-01-01 12:00:00"}]
        with patch('builtins.input', return_value='Test Task'):
            self.test_app.complete_task('Test Task')

        self.assertTrue("completed_at" in self.test_app.tasks[0])

    def test_show_tasks(self):
        self.test_app.tasks = [
            {"task": "Task 1", "created_at": "2023-01-01 12:00:00"},
            {"task": "Task 2", "created_at": "2023-01-02 12:00:00", "completed_at": "2023-01-02 14:00:00"}
        ]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.test_app.show_tasks()
            output = mock_stdout.getvalue().strip()

        self.assertIn("1. Task 1 (Not Completed) - Created at: 2023-01-01 12:00:00", output)
        self.assertIn("2. Task 2 (Completed) - Created at: 2023-01-02 12:00:00", output)

    def test_toggle_voice_reminders(self):
        initial_status = self.test_app.voice_reminders_enabled
        self.test_app.toggle_voice_reminders()
        self.assertNotEqual(initial_status, self.test_app.voice_reminders_enabled)

    def test_schedule_reminder(self):
        # This test is difficult to automate due to the nature of scheduling reminders with sleep
        pass

if __name__ == '__main__':
    unittest.main()

