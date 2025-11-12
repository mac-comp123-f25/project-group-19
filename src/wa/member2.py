import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Planner")
        self.Label1 = tk.Label(self.mainWin, text="Hello World!")
        self.Label1.pack(fill=x, expand=True)  # Common options

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()