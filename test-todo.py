import unittest
from unittest.mock import patch, MagicMock, call, mock_open
from todo import ToDoApp  # assuming the code is in a file called todo_app.py

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.app = ToDoApp()

    @patch('builtins.print')
    def test_display_menu(self, mock_print):
        self.app.display_menu()
        expected_calls = [
            call("\n===== To-Do App Menu ====="),
            call("1. Add Task"),
            call("2. View Tasks"),
            call("3. Mark Task as Completed"),
            call("4. Remove Task"),
            call("5. Exit")
        ]
        mock_print.assert_has_calls(expected_calls, any_order=True)

    @patch('builtins.input', side_effect=["Task 1", "2022-01-01 12:00"])
    def test_add_task(self, mock_input):
        self.app.add_task()
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0]["name"], "Task 1")
        self.assertEqual(self.app.tasks[0]["due_date"], "2022-01-01 12:00")
        self.assertFalse(self.app.tasks[0]["completed"])

    def test_view_tasks(self):
        self.app.tasks = [{"name": "Task 1", "due_date": "2024-06-06 12:00", "completed": False}]
        with patch('builtins.print') as mock_print:
            self.app.view_tasks()
            expected_calls = [
                call("\n===== Tasks ====="),
                call("1. Task 1 - Due: 2024-06-06 12:00 - Status: Pending")
            ]
            mock_print.assert_has_calls(expected_calls, any_order=True)

    @patch('builtins.input', return_value="1")
    @patch('todo.Task.get_task_by_id')
    @patch('todo.Task.mark_completed')
    def test_mark_as_completed(self, mock_mark_completed, mock_get_task_by_id, mock_input):
        mock_task = MagicMock()
        mock_get_task_by_id.return_value = mock_task
        self.app.mark_as_completed()
        mock_get_task_by_id.assert_called_once_with(1)
        mock_mark_completed.assert_called_once_with(mock_task)

    @patch('builtins.input', return_value="1")
    @patch('todo.Task.get_task_by_id')
    @patch('todo.Task.remove')
    def test_remove_task(self, mock_remove, mock_get_task_by_id, mock_input):
        mock_get_task_by_id.return_value = MagicMock()
        self.app.remove_task()
        mock_get_task_by_id.assert_called_once_with(1)
        mock_remove.assert_called_once_with(mock_get_task_by_id.return_value)

    @patch('json.dump')
    def test_save_data(self, mock_dump):
        self.app.tasks = [{"name": "Task 1", "due_date": "2024-06-06 12:00", "completed": False}]
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            self.app.save_data()
            mock_dump.assert_called_once_with(self.app.tasks, mock_file())

    @patch('json.load', return_value=[{"name": "Task 1", "due_date": "2024-06-06 12:00", "completed": False}])
    def test_load_data(self, mock_load):
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            self.app.load_data()
            self.assertEqual(len(self.app.tasks), 1)
            self.assertEqual(self.app.tasks[0]["name"], "Task 1")
            self.assertEqual(self.app.tasks[0]["due_date"], "2024-06-06 12:00")
            self.assertFalse(self.app.tasks[0]["completed"])

if __name__ == "__main__":
    unittest.main()
