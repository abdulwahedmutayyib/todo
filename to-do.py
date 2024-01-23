import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import pyttsx3
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.username = None
        self.tasks = []
        self.load_user_data()
        self.create_widgets()

    def create_widgets(self):
        if not self.username:
            self.show_login_page()
        else:
            self.show_main_page()

    def show_login_page(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, pady=10)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, pady=10)

        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=10)

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=2, column=1, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate username and password (you may implement more secure methods)
        if self.validate_credentials(username, password):
            self.username = username
            self.save_user_data()
            self.login_frame.destroy()
            self.show_main_page()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def validate_credentials(self, username, password):
        # Implement your authentication logic here
        # For simplicity, check if the username is not empty
        return bool(username)

    def show_main_page(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text=f"Welcome, {self.username}!").grid(row=0, column=0, columnspan=4, pady=10)

        # Rest of the code remains the same

    # Rest of the methods remain the same

    def save_user_data(self):
        user_data = {"username": self.username, "tasks": self.tasks}
        with open(f"{self.username}_data.json", "w") as file:
            json.dump(user_data, file)

    def load_user_data(self):
        try:
            with open(f"{self.username}_data.json", "r") as file:
                user_data = json.load(file)
                self.username = user_data["username"]
                self.tasks = user_data["tasks"]
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle file not found or invalid JSON gracefully
            pass

# Create the main window
root = tk.Tk()

# Create the ToDoApp instance
app = ToDoApp(root)

# Run the Tkinter main loop
root.mainloop()
