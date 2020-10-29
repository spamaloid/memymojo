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
buttonOK=Button(root, text='OK')
button_quit = Button(root, text="exit", command = root.destroy)

buttonForward.grid(row=1, column=2)
buttonBack.grid(row=1, column=0)
buttonOK.grid(row=1, column=1)
button_quit.grid(row=2, column=1)

def forward(image_number):
    global myLabel
    global buttonForward
    global buttonBack
    myLabel.grid_forget()
    if image_number==6:
        buttonForward=Button(root, text=">>", state=DISABLED)
    myLabel=Label(image=image_list[image_number-1])
    buttonForward=Button(root, text=">>", command=lambda: forward(image_number+1))
    buttonBack=Button(root, text="<<",command=lambda: back(image_number-1))
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)


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

root.mainloop()
                           
