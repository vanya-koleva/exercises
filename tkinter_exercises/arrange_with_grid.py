# Write a Python program that arranges widgets using the Grid geometry manager with rows and columns.
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter!")

label1 = tk.Label(root, text="First Label")
label2 = tk.Label(root, text="Second Label")
label3 = tk.Label(root, text="Third Label")
label4 = tk.Label(root, text="Fourth Label")
label5 = tk.Label(root, text="Fifth Label")

label1.grid(row=0, column=0, columnspan=2)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)
label4.grid(row=2, column=0)
label5.grid(row=2, column=1)

root.mainloop()
