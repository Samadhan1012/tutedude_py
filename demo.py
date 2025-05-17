# step1: importing
from tkinter import *

# step2: GUI interaction
window = Tk()
window.geometry('500x500')

# step3: adding inputs

# ENTRY BOX
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# BUTTONS

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text='1', width=12, command = lambda:click(1))
b.place(x=10, y=60)

b = Button(window, text='2', width=12, command = lambda:click(2))
b.place(x=85, y=60)

b = Button(window, text='3', width=12, command = lambda:click(3))
b.place(x=160, y=60)

b = Button(window, text='4', width=12, command = lambda:click(4))
b.place(x=10, y=100)

b = Button(window, text='5', width=12, command = lambda:click(5))
b.place(x=85, y=100)

b = Button(window, text='6', width=12, command = lambda:click(6))
b.place(x=160, y=100)

b = Button(window, text='7', width=12, command = lambda:click(7))
b.place(x=10, y=140)

b = Button(window, text='8', width=12, command = lambda:click(8))
b.place(x=85, y=140)

b = Button(window, text='9', width=12, command = lambda:click(9))
b.place(x=160, y=140)

b = Button(window, text='0', width=12, command = lambda:click(0))
b.place(x=10, y=180)

# OPERATORS
def add():
    n1 = e.get()
    global math 
    math = "addition"
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='+', width=12, command=add)
b.place(x=85, y=180)

def sub():
    n1 = e.get()
    global math 
    math = "subtraction"    
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='-', width=12, command=sub)
b.place(x=160, y=180)

def mul():
    n1 = e.get()
    global math 
    math = "multiplication"    
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='*', width=12, command=mul)
b.place(x=10, y=220)

def div():
    n1 = e.get()
    global math 
    math = "division"    
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='/', width=12, command=div)
b.place(x=85, y=220)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))

b = Button(window, text='=', width=12, command=equal)
b.place(x=160, y=220)

def clear():
    e.delete(0, END)

b = Button(window, text='Clear', width=33, command=clear)
b.place(x=10, y=260)

# step4: Mainloop
window.mainloop()
