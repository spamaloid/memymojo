from tkinter import *

root = Tk()
root.title("Radiobutton test")
topFrame=Frame(root)
bottomFrame=Frame(root)

TOPPINGS=[
    ("Cheese","cheese"),
    ("Mushroom","mushroom"),
    ("Pepper","pepper"),
    ("Anchovy","anchovy")]

def clicked(value):
    myLabel=Label(bottomFrame,text=value).pack(anchor=W)

myButton=Button(topFrame, text="Click here", command=lambda:clicked(pizza.get())).pack(padx=10,pady=10, anchor=S)
pizza=StringVar()
for text, topping in TOPPINGS:
    Radiobutton(topFrame, text=text, variable=pizza, value=topping).pack(anchor=W)
    
#clear button does not work properly    
cbutton=Button(topFrame, text="Clear", command=bottomFrame.forget).pack(anchor=N)
qbutton=Button(topFrame, text="Exit", command=root.destroy).pack(anchor=S)
topFrame.pack(padx=20, pady=20, anchor=N)
bottomFrame.pack(padx=20, pady=20, anchor=S)
root.mainloop()    
    
