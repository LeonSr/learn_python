from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("you have ordered : ")
    for index in food:
        print(index)    

    # print("you ordered "+str(listbox.get(listbox.curselection())))

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())
    

window = Tk()

listbox = Listbox(window,bg="#f7ffde",font=('constantia',35),width=12,selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"hamburger")
listbox.insert(3,"hotdog")
listbox.insert(4,"pasta")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

button = Button(window,text='submit',command=submit)
button.pack()


add_button = Button(window,text='add',command=add)
add_button.pack()

del_button = Button(window,text='delete',command=delete)
del_button.pack()

window.mainloop()

