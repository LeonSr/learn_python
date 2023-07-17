from tkinter import *

def submit():
    print("the temperature is: "+str(scale.get())+" degrees C")

window = Tk()

from PIL import ImageTk, Image
hot_img = ImageTk.PhotoImage(Image.open("hot.jpg"))
hotlabel = Label(image=hot_img)
hotlabel.pack(side=TOP)

scale = Scale(
    window,
    from_=100,
    to=0,
    length=400,
    width=40,
    orient=VERTICAL,
    font=('consolas',20),
    tickinterval = 10 ,
    showvalue = 1,
    troughcolor='#69EAFF',
    fg= '#ff1c00',
    bg='#111111'
)

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack(side=TOP)

cold_img = ImageTk.PhotoImage(Image.open("cold.png"))
coldlabel = Label(image=cold_img)
coldlabel.pack(side=TOP)

button = Button(
    window,
    text="submit",
    command=submit,
)
button.pack(side=TOP)

window.mainloop()