#range problem. DISABLED not working
from tkinter import *

root = Tk()
root.title=("Image experiment")

my_img1=PhotoImage(file='image1.gif')
my_img2=PhotoImage(file='image2.gif')
my_img3=PhotoImage(file='image3.gif')
my_img4=PhotoImage(file='image4.gif')
my_img5=PhotoImage(file='image5.gif')
my_img6=PhotoImage(file='image6.gif')
my_img7=PhotoImage(file='image7.gif')

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

myLabel=Label(image=my_img1)
myLabel.grid(row=0, column=0, columnspan=3)

buttonForward=Button(root, text=">>", command=lambda: forward(2))
buttonBack=Button(root, text="<<", command=lambda: back(0))
buttonOK=Button(root, text='Exit', command=root.destroy)
'''buttonQuit=Button(root, text="Stop", command=root.destroy)'''
status=Label(root, text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
buttonForward.grid(row=1, column=2)
buttonBack.grid(row=1, column=0)
buttonOK.grid(row=1, column=1, pady=10)
'''buttonQuit.grid(row=2, column=1, pady=10)'''

def forward(image_number):
    global myLabel
    global buttonForward
    global buttonBack
    myLabel.grid_forget()
    if image_number>=6:
        buttonForward=Button(root, text=">>", state=DISABLED)
    myLabel=Label(image=image_list[image_number-1])
    buttonForward=Button(root, text=">>", command=lambda: forward(image_number+1))
    buttonBack=Button(root, text="<<",command=lambda: back(image_number-1))
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)
    status=Label(root, text="Image "+str(image_number)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global myLabel
    global buttonForward
    global buttonBack

    myLabel.grid_forget()
    if image_number==1:
        buttonBack=Button(root, text="<<",state=DISABLED)
    myLabel=Label(image=image_list[image_number-1])
    buttonForward=Button(root, text=">>",command=lambda: forward(image_number+1))
    buttonBack=Button(root, text="<<",command=lambda: back(image_number-1))

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)
    status=Label(root, text="Image "+str(image_number)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
                           
