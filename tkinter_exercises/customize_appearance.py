# Write a Python program that customizes
# the appearance of labels and buttons (e.g., fonts, colors) using Tkinter.
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter!")

my_label = tk.Label(root, text="This is a label", font=("TimesNewRoman", 17), fg="White", bg="#000000")
my_label.pack()

my_button = tk.Button(root, text="This is a button", font=("Ariel", 14), fg="Black", bg="Pink")
my_button.pack()

root.mainloop()
