import turtle
import tkinter as tk
from tkinter import font as tkFont

#turtle
window = turtle.Screen()
turt = turtle.Turtle()

#font
root = tk.Tk()
label = tk.Label(root, text="Change my font!")
label.pack()

#background color
porcelain = "#F4F4ED"
bright_lavender = "#B388EB"
peach_cream = "#fff0da"
lavender_veil = "#F1E3F3"
window.bgcolor(lavender_veil)

#change font
def change_font():
    new_font = tkFont.Font(family="Verdana", size=20, slant="italic")
    label.config(font=new_font)

#button
button = tk.Button(root, text="Change Font", command=change_font)
button.pack()
root.mainloop()

#keep the window open until close manually
window.exitonclick()
