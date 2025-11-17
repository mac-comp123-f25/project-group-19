import tkinter as tk
from tkinter import simpledialog

# Create the list for tasks to be stored in
tasklist = []

# Set up task object with the properties name and due (date)
class Task:
    def __init__(self, name, due):
        self.name = name
        self.due = due

#  method to make task and then add it to the task list
def make_task(name, due):
    task = Task(name, due)
    tasklist.append(task)

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Planner")
        # button to add tasks
        self.add_button = tk.Button(self.mainWin, text="Add Task", command=self.add_response)
        self.add_button.grid(row=0, column=0)
        # current_row is so that we don't add multiple tasks on the same row
        self.current_row = 1
        #these set up padding so it looks less hideous
        self.mainWin.columnconfigure(1, pad=50)
        self.mainWin.columnconfigure(2, pad=50)
        #i don't think we use this but i haven't tested it
        self.tasks = []

    #runs the window
    def run(self):
        self.mainWin.mainloop()

    #code for adding a task
    def add_response(self):
        #prompts user for task name
        task_name = simpledialog.askstring("Add Task", "Enter Task Name:")
        if task_name:
            #prompts user for due date
            due_date = simpledialog.askstring("Add Task", "Enter Due Date:")
            if due_date:
                #creates the task object
                make_task(task_name, due_date)
                # creates a label with the name of the task
                self.name = tk.Label(self.mainWin, text=task_name)
                #creates a label with the due date
                self.due_date = tk.Label(self.mainWin, text=due_date)
                #places both of those labels in columns 1 and 2 and the row is current_row
                self.name.grid(row=self.current_row, column=1)
                self.due_date.grid(row=self.current_row, column=2)
                #creates a checkbox next to the task and due date
                self.checkbox = tk.Checkbutton(self.mainWin, text="Complete?")
                #places the checkbox in column 3 and the row is current_row
                self.checkbox.grid(row=self.current_row, column=3)
                #Important: current_row is incremented after each task so that they don't get placed
                #in the same row
                self.current_row += 1
                # temp_dict = {self.name.}

    def remove_task(self):
        #TODO: implement this
        pass



# ----- Main program -----
myGui = BasicGui()
myGui.run()

