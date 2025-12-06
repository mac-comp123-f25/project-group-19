import tkinter as tk
from tkinter import simpledialog
from src.wa.helen import save_tasks
from src.wa.helen import get_tasks

# Create the list for tasks to be stored in
tasklist = []

# Get current tasks to save
saved_tasks = get_tasks()

class Task:
    def __init__(self, name, due):
        """Initialize the task with a name and due date"""
        self.name = name
        self.due = due


def make_task(name, due):
    """Create a task object and add it to the tasklist"""
    task = Task(name, due)
    tasklist.append((task.name,task.due)) #adds as a tuple so that it saves nicely
    return task


# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        """Initialize the GUI window and add buttons"""
        self.mainWin = tk.Tk()
        self.mainWin.geometry("500x300")
        self.mainWin.attributes('-topmost', True)  # Force it to be the top layer
        self.mainWin.update()  # Force Tkinter to draw it there immediately
        self.mainWin.after(2000, lambda: self.mainWin.attributes('-topmost', False))
        self.mainWin.lift()
        self.mainWin.title("Task List")

        self.add_button = tk.Button(self.mainWin, text="New Task", command=self.query_user)
        self.add_button.grid(row=0, column=1,pady=10)

        self.close_button = tk.Button(self.mainWin, text="Save and Close", command=self.save_and_close)
        self.close_button.grid(row=0,column=2,pady=10)
        self.current_row = 2

        self.mainWin.columnconfigure(1, pad=50)
        self.mainWin.columnconfigure(2, pad=50)

        self.color_button = tk.Button(
            self.mainWin,
            text="Change background color",
            command=self.change_color
        )
        self.color_button.grid(row=0, column=3,pady=10)

        self.title1 = tk.Label(self.mainWin,text="Task Name",font=("Helvetica",14,"bold"))
        self.title1.grid(row=1,column=1,pady=10)

        self.title2 = tk.Label(self.mainWin,text="Task Due Date",font=("Helvetica",14,"bold"))
        self.title2.grid(row=1,column=2,pady=10)

        self.title3 = tk.Label(self.mainWin,text="Task Complete?",font=("Helvetica",14,"bold"))
        self.title3.grid(row=1,column=3,pady=10)

        for task in saved_tasks:
            self.add_response(task[0], task[1])

    def run(self):
        """Start the GUI"""
        self.mainWin.mainloop()

    def query_user(self):
        """Prompt user for task name and due date"""
        task_name = simpledialog.askstring("Add Task", "Enter Task Name:")
        if task_name:
            due_date = simpledialog.askstring("Add Task", "Enter Due Date:")
            if due_date:
                self.add_response(task_name, due_date)

    def add_response(self, task_name, due_date):
        """Add a task to the GUI and the tasklist"""
        # Create task data
        new_task_object = make_task(task_name, due_date)

        # Create widgets
        name_label = tk.Label(self.mainWin, text=task_name)
        date_label = tk.Label(self.mainWin, text=due_date)
        checkbox = tk.Checkbutton(self.mainWin, text="Complete?")

        # Group widgets to delete
        widgets_to_delete = [name_label, date_label, checkbox]

        # Configure the checkbox to trigger deletion
        # use a lambda to pass the specific items to the remove function
        checkbox.config(command=lambda: self.remove_task(new_task_object, widgets_to_delete))

        # Place on Grid
        name_label.grid(row=self.current_row, column=1)
        date_label.grid(row=self.current_row, column=2)
        checkbox.grid(row=self.current_row, column=3)

        self.current_row += 1


    def remove_task(self, task_object, widget_list):
        """Remove a task from the GUI and the tasklist"""
        # Add a small delay so the user sees the checkmark before it vanishes
        self.mainWin.after(500, lambda: self._perform_deletion(task_object, widget_list))

    def _perform_deletion(self, task_object, widget_list):
        # Remove GUI element
        for widget in widget_list:
            widget.destroy()

        # Save the object's variables into a tuple
        task_tuple_to_remove = (task_object.name, task_object.due)

        # Remove that tuple
        if task_tuple_to_remove in tasklist:
            tasklist.remove(task_tuple_to_remove)

    def save_and_close(self):
        save_tasks(tasklist)
        self.mainWin.destroy()

    def change_color(self):
        color_name = simpledialog.askstring("Add Background Color", "Enter The Hex Color Code:")
        if color_name:
            if color_name[0] != "#":
                color_name = "#" + color_name
            self.mainWin.config(bg=color_name)
            self.color_button.config(highlightbackground=color_name)

# ----- Main program -----
myGui = BasicGui()
myGui.run()