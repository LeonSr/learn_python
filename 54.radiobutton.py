from tkinter import *

def order():
    if(x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("you ordered hamburger")
    elif(x.get()==2):
        print("you ordered hotdog")
    else:
        print("not ordered")


food = ["pizza","hamburger","hotdog"]

window = Tk()

from PIL import ImageTk, Image
pizza_img = ImageTk.PhotoImage(Image.open("pizza.jpg"))
hamburger_img = ImageTk.PhotoImage(Image.open("hamburger.jpg"))
hotdog_img = ImageTk.PhotoImage(Image.open("hotdog.jpg"))

foodimage = [pizza_img,hamburger_img,hotdog_img]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx = 25,
                              font=('Impact',50),
                              image=foodimage[index],
                              compound='left',
                              bg="white",
                              indicatoron=0,
                              width=375,
                              command=order
                              )
    
    radiobutton.pack(anchor=W)














window.mainloop()


