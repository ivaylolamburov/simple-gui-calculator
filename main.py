from tkinter import *


def buttonClick(value):
    global x, y, sign, error
    if value == 'clear':
        calcInput.delete(0, END)
        x = 0
        y = 0
    else:
        if type(value) is int or type(value) is float or value == '.':
            current = calcInput.get()
            calcInput.delete(0, END)
            calcInput.insert(0, str(current) + str(value))
        else:
            if value != '=':
                sign = value
                try:
                    x = float(calcInput.get())
                except ValueError:
                    x = 0
                finally:
                    calcInput.delete(0, END)
            if value == '=':
                try:
                    y = float(calcInput.get())
                except ValueError:
                    y = 0
                finally:
                    calcInput.delete(0, END)
                    try:
                        dev = x / y
                    except ZeroDivisionError:
                        dev = 0
                    cases = {
                        '+': x + y,
                        '-': x - y,
                        '*': x * y,
                        '/': dev
                    }
                    for key, result in cases.items():
                        if sign == key:
                            calcInput.insert(0, result)


# define the window
root = Tk()
root.title('Simple Calculator')
root.iconbitmap(default='icon.ico')  # define window icon

calcInput = Entry(root, width=40, borderwidth=5)
calcInput.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text=' 3 ', padx=39, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text=' 6 ', padx=39, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text=' 9 ', padx=39, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text=' 0 ', padx=86, pady=20, command=lambda: buttonClick(0))

decimalButton = Button(root, text=' .  ', padx=39, pady=20, command=lambda: buttonClick('.'))
clearButton = Button(root, text='Clear ', padx=77, pady=20, command=lambda: buttonClick('clear'))
plusButton = Button(root, text=' +  ', padx=36, pady=20, command=lambda: buttonClick('+'))
equalButton = Button(root, text='   =   ', padx=81, pady=20, command=lambda: buttonClick('='))
minusButton = Button(root, text=' - ', padx=39, pady=20, command=lambda: buttonClick('-'))
multiButton = Button(root, text=' * ', padx=39, pady=20, command=lambda: buttonClick('*'))
divButton = Button(root, text=' / ', padx=39, pady=20, command=lambda: buttonClick('/'))

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0, columnspan=2)
decimalButton.grid(row=4, column=2)

plusButton.grid(row=1, column=3)
minusButton.grid(row=2, column=3)
multiButton.grid(row=3, column=3)
divButton.grid(row=4, column=3)

equalButton.grid(row=5, column=2, columnspan=2)
clearButton.grid(row=5, column=0, columnspan=2)

# main loop
root.mainloop()
