import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter!")

my_button = tk.Button(root, text="Quit", command=root.destroy)
my_button.pack()

root.mainloop()
