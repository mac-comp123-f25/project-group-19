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
        self.add_button.grid(row=0, column=0, sticky = "W")

        self.close_button = tk.Button(self.mainWin, text="Save and Close", command=self.save_and_close)
        self.close_button.grid(row=1,column=0, sticky = "W")
        self.current_row = 1

        self.mainWin.columnconfigure(1, pad=50)
        self.mainWin.columnconfigure(2, pad=50)

        self.color_button = tk.Button(
            self.mainWin,
            text="Change background color",
            command=self.change_color
        )
        self.color_button.grid(row=2, column=0, sticky = "W")

        self.gui_rows = []

        # Adds saved tasks to the GUI
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
        self.gui_rows.append([name_label, date_label, checkbox])

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
        self.mainWin.after(500, lambda: self.perform_deletion(task_object, widget_list))

    def perform_deletion(self, task_object, widget_list):
        """Remove the GUI elements and the task from the tasklist"""
        # Remove GUI element
        del_row_index = self.gui_rows.index(widget_list)
        del self.gui_rows[del_row_index]
        for row in self.gui_rows[del_row_index:]:
            row[0].grid(column = 1, row = row[0].grid_info()["row"] - 1)
            row[1].grid(column = 2, row = row[1].grid_info()["row"] - 1)
            row[2].grid(column = 3, row = row[2].grid_info()["row"] - 1)
        self.current_row -= 1
        for widget in widget_list:
            widget.destroy()

        task_tuple = (task_object.name, task_object.due)
        if task_tuple in tasklist:
            tasklist.remove(task_tuple)

        # Save the object's variables into a tuple
        task_tuple_to_remove = (task_object.name, task_object.due)

        # Remove that tuple
        if task_tuple_to_remove in tasklist:
            tasklist.remove(task_tuple_to_remove)

    def save_and_close(self):
        """Save the tasklist and close the window"""
        save_tasks(tasklist)
        self.mainWin.destroy()

    def change_color(self):
        """Change the background color of the window"""
        color_name = simpledialog.askstring("Add Background Color", "Enter The Hex Color Code:")
        if color_name:
            # Handles missing "#" at the beginning of the color code
            if color_name[0] != "#":
                color_name = "#" + color_name
            # Changes the background color of the window
            self.mainWin.config(bg=color_name)
            # Changes the color of the buttons as well
            self.color_button.config(highlightbackground=color_name)
            self.close_button.config(highlightbackground=color_name)
            self.add_button.config(highlightbackground=color_name)

# ----- Main program -----
myGui = BasicGui()
myGui.run()