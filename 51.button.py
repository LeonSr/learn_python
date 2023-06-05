from tkinter import *

count = 0

def click():
    global count
    count +=1
    print(count)

window = Tk()

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("logo.png"))


button = Button(window,
                text="click me!",
                command=click,
                font=("comic sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image= img,
                compound="top"
                )

button.pack()



window.mainloop()
