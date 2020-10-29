from tkinter import *
import tkinter.messagebox

class MyGui:
    def __init__(self):
    
        self.root = Tk()
        self.topFrame=tkinter.Frame(self.root)
        self.bottomFrame=tkinter.Frame(self.root)
        
        self.myLabel1 = Label(self.topFrame, text="hello")
        self.myLabel2 = Label(self.topFrame, text="how are you?")
        self.quitbutton = Button(self.bottomFrame, text="Exit", command=self.root.destroy)
        self.okbutton=Button(self.bottomFrame, text='OK', command=self.show_choice)

        self.myLabel1.grid(row=0, column=0)
        self.myLabel2.grid(row=0, column=1)
        self.quitbutton.grid(row=2, column=0)
        self.okbutton.grid(row=1, column=0)

        self.cb_var1=tkinter.IntVar()
        self.cb_var2=tkinter.IntVar()
        self.cb_var3=tkinter.IntVar()
        
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        
        self.cb1=tkinter.Checkbutton(self.topFrame, text='One', variable=self.cb_var1)
        self.cb2=tkinter.Checkbutton(self.topFrame, text='Two', variable=self.cb_var2)
        self.cb3=tkinter.Checkbutton(self.topFrame, text='Three', variable=self.cb_var3)
        
        self.cb1.grid(row=4, column=1)
        self.cb2.grid(row=5, column=1)
        self.cb3.grid(row=6, column=1)

        self.topFrame.pack()
        self.bottomFrame.pack()

        tkinter.mainloop()

    def show_choice(self):
        self.message='You selected: \n'
        if self.cb_var1.get()==1:
            self.message=self.message+'1 \n'
        if self.cb_var2.get()==1:
            self.message =self.message+'2 \n'
        if self.cb_var3.get()==1:
            self.message=self.message+'3 \n'
        tkinter.messagebox.showinfo('Selection', self.message)
   
my_gui = MyGui()
