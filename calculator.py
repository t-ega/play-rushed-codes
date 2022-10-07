from tkinter import *
import math

root = Tk()
root.title("Tegas Calculator")

f_num = ' '
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, pady=10, padx=45)


def op(inp, no):
    global f_num
    global maths
    f_num = e.get()
    maths = inp
    e.delete(0,END)


def onclick(number):
    e.insert(END, number)


def calc(number):
   if maths == '+':
      ans = getdouble(number) + getdouble(f_num)
      e.delete(0, END)
      e.insert(0, ans)
   elif maths == '-':
      ans = getdouble(f_num) - getdouble(number)
      e.delete(0, END)
      e.insert(0, ans)
   elif maths == '/':
      try:
         ans = getdouble(f_num) / getdouble(number)
         e.delete(0, END)
         e.insert(0, int(ans))
      except ZeroDivisionError:
         e.delete(0, END)
         e.insert(0, "CANNOT DIVIDE BY ZERO!")
   elif maths == 'x':
      ans = getdouble(f_num) * getdouble(number)
      e.delete(0, END)
      e.insert(0, ans)
   elif maths == 'p':
      ans = pow(getdouble(f_num), getdouble(number))
      e.delete(0, END)
      e.insert(0, ans)
def clr():
    e.delete(0, END)

one = Button(root, text="1", padx=30, pady=15, command=lambda: onclick(1)).grid(row=3, column=0)
two = Button(root, text="2", padx=30, pady=15, command=lambda: onclick(2)).grid(row=3, column=1)
three = Button(root, text="3", padx=30, pady=15, command=lambda: onclick(3)).grid(row=3, column=2)

four = Button(root, text="4", padx=30, pady=15, command=lambda: onclick(4)).grid(row=2, column=0)
five = Button(root, text="5", padx=30, pady=15, command=lambda: onclick(5)).grid(row=2, column=1)
six = Button(root, text="6", padx=30, pady=15, command=lambda: onclick(6)).grid(row=2, column=2)

seven = Button(root, text="7", padx=30, pady=15, command=lambda: onclick(7)).grid(row=1, column=0)
eight = Button(root, text="8", padx=30, pady=15, command=lambda: onclick(8)).grid(row=1, column=1)
nine = Button(root, text="9", padx=30, pady=15, command=lambda: onclick(9)).grid(row=1, column=2)

zero = Button(root, text='0', padx=30, pady=15, command=lambda: onclick(0)).grid(row=4, column=0)


# Function Buttons-->
mult = Button(root, text = "X", padx=30,pady=15, command=lambda: op('x', e.get())).grid(row=4,column=1)
clr = Button(root, text = "CE", padx=30,pady=15, command=clr).grid(row=4,column=4)
sub = Button(root, text='-', padx=30, pady=15, command=lambda: op('-', e.get())).grid(row=2, column=4)
div = Button(root, text='/', padx=30, pady=15, command=lambda: op('/', e.get())).grid(row=4, column=2)
add = Button(root, text='+', padx=30, pady=15, command=lambda: op('+', e.get()))
add.grid(row=1, column=4)
rtt= Button(root, text='root', padx=30, pady=15, command=lambda: op('r', e.get())).grid(row=5, column=1)
dot = Button(root, text='.', padx=30, pady=15, command=lambda:onclick('.')).grid(row=4, column=2)
power = Button(root, text='pow', padx=30, pady=15, command=lambda: op('p', e.get())).grid(row=5, column=0)
equal = Button(root, text='=', padx=30, pady=15, bg = "light blue" , fg= "white", command=lambda: calc(e.get())).grid(row=3, column=4)
ans = Button(root,text='ANS', padx=30, pady=15, command=lambda: calc(e.get())).grid(row=5,column=3,columnspan=2)
#


root.mainloop()
