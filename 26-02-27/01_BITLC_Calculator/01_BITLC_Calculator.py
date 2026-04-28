#26-02-27_01_calculator
from tkinter import *
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="black")
    root.title("BITLC Calculator")
    root.geometry("512x256") #from 270x150

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=10, ipadx=256)

    # Number buttons
    btn1 = Button(root, text='1', fg='black', bg='#E1D9D1', command=lambda: press(1), height=2, width=10)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='#E1D9D1', command=lambda: press(2), height=2, width=10)
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='black', bg='#E1D9D1', command=lambda: press(3), height=2, width=10)
    btn3.grid(row=2, column=2)
    btn4 = Button(root, text='4', fg='black', bg='#E1D9D1', command=lambda: press(4), height=2, width=10)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='black', bg='#E1D9D1', command=lambda: press(5), height=2, width=10)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='black', bg='#E1D9D1', command=lambda: press(6), height=2, width=10)
    btn6.grid(row=3, column=2)
    btn7 = Button(root, text='7', fg='black', bg='#E1D9D1', command=lambda: press(7), height=2, width=10)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='black', bg='#E1D9D1', command=lambda: press(8), height=2, width=10)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='black', bg='#E1D9D1', command=lambda: press(9), height=2, width=10)
    btn9.grid(row=4, column=2)
    btn0 = Button(root, text='0', fg='black', bg='#E1D9D1', command=lambda: press(0), height=2, width=10)
    btn0.grid(row=5, column=1)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='#006400', command=lambda: press('+'), height=2, width=10)
    plus.grid(row=1, column=3)
    minus = Button(root, text='-', fg='black', bg='#006400', command=lambda: press('-'), height=2, width=10)
    minus.grid(row=2, column=3)
    mult = Button(root, text='*', fg='black', bg='#006400', command=lambda: press('*'), height=2, width=10)
    mult.grid(row=3, column=3)
    div = Button(root, text='/', fg='black', bg='#006400', command=lambda: press('/'), height=2, width=10)
    div.grid(row=4, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=2, width=10)
    eq.grid(row=5, column=3)
    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=2, width=10)
    clr.grid(row=1, column=0)
    dot = Button(root, text='.', fg='black', bg='#006400', command=lambda: press('.'), height=2, width=10)
    dot.grid(row=5, column=2)

    root.mainloop()
