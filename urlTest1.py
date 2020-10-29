from tkinter import *
import webbrowser

url='https://www.ecosia.org'
root=Tk()
root.geometry("400x400")

def openUrl():
    webbrowser.open_new(url)

def openWin():
    win2=Tk()
    win2.geometry("400x500")
    
    uButton=Button(win2, text='Open Ecosia', command=openUrl)
    uButton.grid(row=1, column=0)
        
    qButton=Button(win2, text="Close window", command=win2.destroy)
    qButton.grid(row=2, column=0)

winButton=Button(root, text="Open window", command=openWin)
winButton.grid(row=2, column=0, padx=15, pady=15)

closeButton=Button(root, text="Close this window", command=root.destroy)
closeButton.grid(row=3, column=0, padx=15, pady=15, ipadx=168)

root.mainloop()
              

