import unittest
import tkinter as tk
from tkinter import Entry, Listbox

from your_todo_app_file import ToDoApp  # Replace with the actual filename

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = ToDoApp(self.root)
        self.app.username = "testuser"
        self.app.show_main_page()

    def tearDown(self):
        self.root.destroy()

    def test_add_task(self):
        task_entry = self.app.task_entry
        task_listbox = self.app.task_listbox

        task_entry.insert(0, "Test Task")
        self.app.add_task()

        self.assertEqual(task_listbox.get(0), "1. Test Task - Due: - Pending")

    def test_remove_task(self):
        task_entry = self.app.task_entry
        task_listbox = self.app.task_listbox

        task_entry.insert(0, "Test Task")
        self.app.add_task()

        task_listbox.select_set(0)
        self.app.remove_task()

        self.assertEqual(task_listbox.size(), 0)

    def test_mark_as_done(self):
        task_entry = self.app.task_entry
        task_listbox = self.app.task_listbox

        task_entry.insert(0, "Test Task")
        self.app.add_task()

        task_listbox.select_set(0)
        self.app.mark_as_done()

        self.assertEqual(task_listbox.get(0), "1. Test Task - Due: - Done")

if __name__ == "__main__":
    unittest.main()
