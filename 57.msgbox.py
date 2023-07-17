from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='message box',message='you are an idiot')
    # messagebox.showwarning(title='warning',message='you have a VIRUS!!!')
    # messagebox.showerror(title='error',message='something went wrong')
    # if messagebox.askokcancel(title='ask ok cancel',message='do you want to do the thing'):
    #     print("you did a thing")
    # else:
    #     print("you didnt do anything")
    # if messagebox.askretrycancel(title='ask retry or no',message='do you want to retry the thing'):
    #     print("you retry a thing")
    # else:
    #     print("you didnt retry anything")
    # if messagebox.askyesno(title='ask yes or no',message='do you like me'): 
    #     print("i like you")
    # else:
    #     print('why dont you like me')
    # print(messagebox.askquestion(title="question",message="do you like me? "))
    print(messagebox.askyesnocancel(title="yes no cancel",message="do you like to code"))
    

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()