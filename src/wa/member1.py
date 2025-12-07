import tkinter as tk
from tkinter import simpledialog
from src.wa.helen import save_tasks, get_tasks


# Create the list for tasks to be stored in
tasklist = []

# Set default label color
label_color = "#000000"

# Need to figure out how to get this list of saved tasks to appear when we open the planner.
saved_tasks = get_tasks()

def make_task(name, due):
    tasklist.append((name,due)) #adds as a tuple so that it saves nicely


def add_data_to_list(name, due):
    # 1. Create a tuple (immutable list) of the data
    task_tuple = (name, due)

    # 2. Add it to the global list that saves to the file
    tasklist.append(task_tuple)

    # 3. Return it so the GUI can use it
    return task_tuple

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("500x300")
        self.mainWin.attributes('-topmost', True)  # 1. Force it to be the top layer
        self.mainWin.update()  # 2. Force Tkinter to draw it there immediately
        self.mainWin.after(2000, lambda: self.mainWin.attributes('-topmost', False))
        self.mainWin.lift()
        self.mainWin.title("Planner")

        self.add_button = tk.Button(self.mainWin, text="New Task", command=self.query_user)
        self.add_button.grid(row=0, column=0)

        #I just put the close button in the grid somewhere. It probably should not go right next to the add button. Fix later.
        self.close_button = tk.Button(self.mainWin, text="Save and Close", command=self.save_and_close)
        self.close_button.grid(row=0,column=1)

        #The .place isn't working.
        self.size_widget=tk.Label(bg='white',text="")
        self.size_widget.place(relx=400,rely=300,anchor='center')

        self.current_row = 1

        self.mainWin.columnconfigure(1, pad=50)
        self.mainWin.columnconfigure(2, pad=50)

        self.color_button = tk.Button(
            self.mainWin,
            text="Change my background color!",
            command=self.change_color
        )
        self.color_button.grid(row=0, column=2)

        for task in saved_tasks:
            self.add_response(task[0], task[1])

    def run(self):
        self.mainWin.mainloop()

    def query_user(self):
        task_name = simpledialog.askstring("Add Task", "Enter Task Name:")
        if task_name:
            due_date = simpledialog.askstring("Add Task", "Enter Due Date:")
            if due_date:
                self.add_response(task_name, due_date)

    def add_response(self, task_name, due_date):
        # Create task data

        current_task_tuple = add_data_to_list(task_name, due_date)

        # Create widgets
        name_label = tk.Label(self.mainWin, text=task_name)
        date_label = tk.Label(self.mainWin, text=due_date)
        checkbox = tk.Checkbutton(self.mainWin, text="Complete?")

        # Group widgets to delete
        widgets_to_delete = [name_label, date_label, checkbox]

        # Configure the checkbox to trigger deletion
        # use a lambda to pass the specific items to the remove function
        checkbox.config(command=lambda: self.remove_task(current_task_tuple, widgets_to_delete))

        # Place on Grid
        name_label.grid(row=self.current_row, column=1)
        date_label.grid(row=self.current_row, column=2)
        checkbox.grid(row=self.current_row, column=3)

        self.current_row += 1

    def remove_task(self, task_object, widget_list):
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