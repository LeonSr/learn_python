from tkinter import *

# label = an area widget that holds text and/or an image within a window


window = Tk()

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("logo.png"))

label = Label(window,
              text="hello world",
              font=('Arial',40,'bold'),
              fg='#00ff00',
              bg='#68dbf7',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=30,
              image = img,
              compound="bottom"
              )

label.pack()

# label.place(x= 100,y = 100)

window.mainloop()