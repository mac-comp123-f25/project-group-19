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
        self.input1 = tk.Entry(self.mainWin)
        self.input1.grid(row=0, column=0)
        self.input1.bind('<Return>', self.entry_response)
        self.input1.bind('<Tab>', self.entry_response)
        self.add_button = tk.Button(self.mainWin, text="Add Task", command=self.add_response)
        self.add_button.grid(row=0, column=1)
        self.current_row = 1

    def run(self):
        self.mainWin.mainloop()

    def entry_response(self, event):
        text = self.input1.get()
        self.input1.delete(0, tk.END)

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
                self.current_row += 1


# ----- Main program -----
myGui = BasicGui()
myGui.run()

