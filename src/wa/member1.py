import tkinter as tk
from tkinter import simpledialog

# Create the list for tasks to be stored in
tasklist = []


class Task:
    def __init__(self, name, due):
        self.name = name
        self.due = due


def make_task(name, due):
    task = Task(name, due)
    tasklist.append(task)
    return task


# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("400x300")
        self.mainWin.title("Planner")

        self.add_button = tk.Button(self.mainWin, text="Add Task", command=self.add_response)
        self.add_button.grid(row=0, column=0)

        self.current_row = 1

        self.mainWin.columnconfigure(1, pad=50)
        self.mainWin.columnconfigure(2, pad=50)

    def run(self):
        self.mainWin.mainloop()

    def add_response(self):
        task_name = simpledialog.askstring("Add Task", "Enter Task Name:")
        if task_name:
            due_date = simpledialog.askstring("Add Task", "Enter Due Date:")
            if due_date:
                # 1. Create task data
                new_task_object = make_task(task_name, due_date)

                # 2. Create widgets (using local variables, not self.)
                name_label = tk.Label(self.mainWin, text=task_name)
                date_label = tk.Label(self.mainWin, text=due_date)
                checkbox = tk.Checkbutton(self.mainWin, text="Complete?")

                # 3. Group widgets to delete
                widgets_to_delete = [name_label, date_label, checkbox]

                # 4. Configure the Checkbox to trigger deletion
                # We use a lambda to pass the specific items to the remove function
                checkbox.config(command=lambda: self.remove_task(new_task_object, widgets_to_delete))

                # 5. Place on Grid
                name_label.grid(row=self.current_row, column=1)
                date_label.grid(row=self.current_row, column=2)
                checkbox.grid(row=self.current_row, column=3)

                self.current_row += 1

    def remove_task(self, task_object, widget_list):
        # Optional: Add a small delay so the user sees the checkmark before it vanishes
        # 500ms = 0.5 seconds
        self.mainWin.after(500, lambda: self._perform_deletion(task_object, widget_list))

    def _perform_deletion(self, task_object, widget_list):
        # actually destroy the widgets and data
        for widget in widget_list:
            widget.destroy()

        if task_object in tasklist:
            tasklist.remove(task_object)
            print(f"Completed: {task_object.name}")


# ----- Main program -----
myGui = BasicGui()
myGui.run()