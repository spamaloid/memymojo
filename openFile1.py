from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("Opening a file")

def open():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="/Users/kimi/Documents/courses/UI/pythonstuff/images", title="Select file", filetypes=(("gif files","*.gif"),("all files","*.*")))
    my_label=Label(root, text=root.filename).pack()
    my_image=PhotoImage(file=root.filename)
    my_image_label=Label(image=my_image).pack()

my_btn=Button(root, text="Open a file", command=open).pack()

root.mainloop()
