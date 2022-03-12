from tkinter import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from tkinter import ttk


def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)


def clear():
    global operator
    operator = ''
    txt_input.set('')
    display.insert(0, '0')


def equal():
    global operator
    sump = float(eval(operator))
    if sump % 1 == 0:
        sump = int(eval(operator))

    txt_input.set(sump)
    operator = ''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Declarations~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

root = Tk()
root.title('מחשבון')
root.resizable(width=0, height=0)
root.columnconfigure((0, 1, 2, 3), weight=1)
root.rowconfigure((1, 2, 3, 4, 5), weight=1)
root.geometry('300x500')

operator = ''
txt_input = StringVar(value='0')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

display = Entry(root, font=('Agency FB', 30, 'bold'), fg='white', bg='green', justify='right',
                bd=50, width=27, textvariable=txt_input)
display.grid(columnspan=4)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Row 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btn1 = Button(root, text='1', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(1),  bd=8, fg='black').grid(row=1, column=0)

btn2 = Button(root, text='2', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(2), bd=8, fg='black').grid(row=1, column=1)

btn3 = Button(root, text='3', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(3), bd=8, fg='black').grid(row=1, column=2)

btnC = Button(root, text='C', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=clear, bd=8, fg='black', bg='green').grid(row=1, column=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Row 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btn4 = Button(root, text='4', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(4), bd=8, fg='black').grid(row=2, column=0)

btn5 = Button(root, text='5', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(5), bd=8, fg='black').grid(row=2, column=1)

btn6 = Button(root, text='6', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(6), bd=8, fg='black').grid(row=2, column=2)

btnP = Button(root, text='+', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn('+'), bd=8, fg='black', bg='Orange').grid(row=2, column=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Row 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btn7 = Button(root, text='7', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(7), bd=8, fg='black').grid(row=3, column=0)

btn8 = Button(root, text='8', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(8), bd=8, fg='black').grid(row=3, column=1)

btn9 = Button(root, text='9', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(9), bd=8, fg='black').grid(row=3, column=2)

btnM = Button(root, text='-', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn('-'), bd=8, fg='black', bg='Orange').grid(row=3, column=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Row 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btnOpenBar = Button(root, text='(', font=('arial', 30, 'bold'), padx=30, pady=15,
                    command=lambda: btn('('), bd=8, fg='black', bg='Orange').grid(row=4, column=0)

btn0 = Button(root, text='0', font=('arial', 30, 'bold'), padx=30, pady=15,
              command=lambda: btn(0), bd=8, fg='black').grid(row=4, column=1)

btnCloseBar = Button(root, text=')', font=('arial', 30, 'bold'), padx=35, pady=15,
                     command=lambda: btn(')'), bd=8, fg='black', bg='Orange').grid(row=4, column=2)

btnMulti = Button(root, text='X', font=('arial', 30, 'bold'), padx=30, pady=15,
                  command=lambda: btn('*'), bd=8, fg='black', bg='Orange').grid(row=4, column=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Row 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

btnEq = Button(root, text='=', font=('arial', 30, 'bold'), padx=103, pady=15,
               command=equal, bd=8, fg='black', bg='green').grid(row=5, column=0, columnspan=2)

btnDot = Button(root, text='.', font=('arial', 30, 'bold'), padx=35, pady=15,
                command=lambda: btn('.'), bd=8, fg='black', bg='orange').grid(row=5, column=2)

btnDiv = Button(root, text='/', font=('arial', 30, 'bold'), padx=30, pady=15,
                command=lambda: btn('/'), bd=8, fg='black', bg='Orange').grid(row=5, column=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

root.mainloop()
