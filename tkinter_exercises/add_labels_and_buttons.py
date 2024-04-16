import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
my_label = tk.Label(root, text="Click the button!")
my_label.pack()


def on_click():
    my_label.config(text="Look! You clicked a button!")


my_button = tk.Button(root, text="Click me!", command=on_click)
my_button.pack()

root.mainloop()
