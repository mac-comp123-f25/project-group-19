import tkinter as tk
from tkinter import simpledialog

TASKLIST = []

class Task:
    def __init__(self, name, due):
        self.name = name
        self.due = due

def make_task(name, due):
    task = Task(name, due)
    add_to_tasklist(TASKLIST, task)

def get_task_name(task):
    return task.name

def get_task_due(task):
    return task.due

def get_task_work_date(task):
    return task.work_date

# category
def get_task_cat(task):
    return task.cat

def get_task_all(task):
    return task

def add_to_tasklist(tasklist, task):
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

    def run(self):
        self.mainWin.mainloop()

    def entry_response(self, event):
        text = self.input1.get()
        self.input1.delete(0, tk.END)

    def add_response(selfs):
        task_name = simpledialog.askstring("Add Task", "Enter Task Name:")
        due_date = simpledialog.askstring("Add Task", "Enter Due Date:")
        make_task(task_name, due_date)
        print(TASKLIST)

# ----- Main program -----
myGui = BasicGui()
myGui.run()
