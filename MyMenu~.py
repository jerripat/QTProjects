from tkinter import *

root = Tk()
root.title("Backup Menu")
root.geometry("450x450")

my_menu = Menu(root)
root.config(menu=my_menu)


def new():
    file_frame.grid(row=1, column=2, padx=10, pady=10)


def cut():
    edit_frame.grid(row=1, column=2, padx=10, pady=10)


def save():
    pass


def copy():
    pass


def paste():
    pass


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# File menu frame

file_frame = Frame(root, width=200, height=200,
                   bd=3, bg="blue", relief="sunken")
#file_frame.grid(row=1, column=2, padx=10, pady=10)
file_frame_label = Label(file_frame, text="File Frame", font=("Arial", 15))
file_frame_label.pack(padx=20, pady=20)

# Edit menu frame
edit_frame = Frame(root, width=200, height=200,
                   bd=3, bg="blue", relief="sunken")
#dit_frame.grid(row=1, column=2, padx=10, pady=10)
edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Arial", 15))
edit_frame_label.pack(padx=20, pady=20)


root.mainloop()
