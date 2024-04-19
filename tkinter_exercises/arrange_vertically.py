# Write a Python program to create a Tkinter window
# with three labels arranged vertically using the Pack geometry manager.
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter!")

label1 = tk.Label(root, text="First Label")
label1.pack(side="top")
label2 = tk.Label(root, text="Second Label")
label2.pack(side="top")
label3 = tk.Label(root, text="Third Label")
label3.pack(side="top")

root.mainloop()