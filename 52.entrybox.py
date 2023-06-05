from tkinter import *

def submit():
   user = entry.get()
   print(user)
   entry.config(state=DISABLED)


def delete():
   entry.delete(0,END)


def backspace():
   entry.delete((len(entry.get()))-1,END)



window = Tk()

entry = Entry(window,
              font = ("arial",50),
              fg="green",
              bg="black",
              show="*")

# entry.insert(0,'test')
entry.pack(side=LEFT)

submit_bt = Button(window,
                text="submit",
                command=submit,
                font=("comic sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                )

submit_bt.pack(side=RIGHT)

backspace_bt = Button(window,
                text="backspace",
                command=backspace,
                font=("comic sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                )

backspace_bt.pack(side=RIGHT)

delete_bt = Button(window,
                text="delete",
                command=delete,
                font=("comic sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                )

delete_bt.pack(side=RIGHT)


window.mainloop()