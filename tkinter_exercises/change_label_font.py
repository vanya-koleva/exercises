# Write a Python GUI program to create a label and
# change the label font style (font name, bold, size) using tkinter module.
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter!")
my_label = tk.Label(root, text="Learning Tkinter", font=("Open Sans", 80))
my_label.grid(row=0, column=0)
root.mainloop()
