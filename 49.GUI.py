from tkinter import *

# widgets = GUL elements : button text box labels image
# windows = serves as a container to hold or contain these widgets

window = Tk()       # instantiate an instance of a window

window.geometry("420x420")      # changing the size of window   

window.title("bro code first GUI program")  # changing the title of the window

#changing the image

# icon = PhotoImage(file='logo.png')         # this one had problem the solution is down
from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("logo.png"))
window.iconphoto(True,img)

window.config(background="#68dbf7")     # changing background of color


window.mainloop()   # place window on computer screen, listen for events





