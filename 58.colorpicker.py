from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorhex = color[1]
    print(colorhex)
    window.config(bg=colorhex)

    # window.config(bg=colorchooser.askcolor()[1])             change bg with one line summery of the last 3 line of code

window = Tk()

window.geometry('420x420')
button = Button(text='clickme',command=click)

button.pack()

window.mainloop()