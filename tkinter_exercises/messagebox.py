# Write a Python program that displays messages in a messagebox using Tkinter.
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Messages")


def display_message():
    messagebox.showinfo("Message:", "Hello World!")


my_button = tk.Button(root, text="Show message", command=display_message)
my_button.pack()

root.mainloop()
