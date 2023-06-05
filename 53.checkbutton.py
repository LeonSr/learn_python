from tkinter import *

def  display():
    if(x.get()==1):
        print("you agree")
    else:
        print("you disagree")

window = Tk()

x = IntVar()

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("python.png"))

check_button = Checkbutton(window,
                           text="i agree",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg="green",
                           bg="black",
                           activebackground="black",
                           activeforeground="green",
                           padx= 40,
                           pady= 40,
                           image=img,
                           compound="left")

check_button.pack()


window.mainloop()