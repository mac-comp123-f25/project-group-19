import tkinter as tk
from tkinter import simpledialog

tasklist = []

class Task:
    def __init__(self, name, due):
        self.name = name
        self.due = due

def make_task(name, due):
    task = Task(name, due)
    tasklist.append(task)

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Planner")
        self.add_button = tk.Button(self.mainWin, text="Add Task", command=self.add_response)
        self.add_button.grid(row=0, column=0)
        self.current_row = 1
        self.mainWin.columnconfigure(1, pad=50)
        self.mainWin.columnconfigure(2, pad=50)
        self.tasks = []

    def run(self):
        self.mainWin.mainloop()

    def add_response(self):
        task_name = simpledialog.askstring("Add Task", "Enter Task Name:")
        if task_name:
            due_date = simpledialog.askstring("Add Task", "Enter Due Date:")
            if due_date:
                make_task(task_name, due_date)
                self.name = tk.Label(self.mainWin, text=task_name)
                self.due_date = tk.Label(self.mainWin, text=due_date)
                self.name.grid(row=self.current_row, column=1)
                self.due_date.grid(row=self.current_row, column=2)
                self.checkbox = tk.Checkbutton(self.mainWin, text="Complete?")
                self.checkbox.grid(row=self.current_row, column=3, command=self.remove_task)
                self.current_row += 1
                temp_dict = {self.name.}

    def remove_task(self):



# ----- Main program -----
myGui = BasicGui()
myGui.run()

