import tkinter as tk
from tkinter import simpledialog

#font
root = tk.Tk()
label = tk.Label(root, text="Change my font!")
label.pack()

#a button that pops up a dialogue box and then input the hex code and then change the background color
class Change_Background_Color:
    def __init__(self):
        self.window = tk.Tk()

        self.color_button = tk.Button(
            self.window,
            text="Change my background color!",
            command=self.change_color
        )
        self.color_button.grid(row=0, column=0, padx=20, pady=20)

    def run(self):
        self.window.mainloop()

    def change_color(self):
        color_name = simpledialog.askstring("Add Background Color", "Enter The Hex Color Code:")
        if color_name:
            self.window.config(bg=color_name)
            self.color_button.config(highlightbackground=color_name)

myGui = Change_Background_Color()
myGui.run()