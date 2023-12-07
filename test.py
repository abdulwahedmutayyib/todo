# test_todolist.py
import unittest
from tkinter import Tk
from todolist import TodoListApp

class TestTodoListApp(unittest.TestCase):
    def setUp(self):
        self.app = Tk()
        self.todo_list = TodoListApp(self.app)

    def test_add_task(self):
        # Test the add_task method
        self.todo_list.entry.insert(0, "Test Task")
        self.todo_list.add_task()
        self.assertEqual(self.todo_list.listbox.get(0), "Test Task")

    # Add more test methods for other functionalities

if __name__ == '__main__':
    unittest.main()

