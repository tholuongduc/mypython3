from tkinter import *

expression = ""
#press number
def press(num):
    global expression
    expression = expression + str(num)
    final_result.set(expression)

def clear():
    global expression
    expression = ""
    final_result.set(expression)

def press_negative():
    global expression
    expression = f'(-{expression})'
    final_result.set(expression)

def press_percent():
    global expression
    expression = str(eval(expression + "/100"))
    final_result.set(expression)

def press_equal():
    try:
        global expression
        total = str(eval(expression))
        final_result.set(total)
        expression = ""
    except:
        final_result.set("Error!")
        expression = ""


cal = Tk()
cal.title("Calculator")
cal.geometry("250x250")

#Result location
final_result = StringVar()
lb_result = Entry(cal, textvariable=final_result, bd=5, justify="right")
lb_result.grid(columnspan=5, ipadx=16)

#Create number board
clear_button = Button(cal, text="AC", width=4, height=2,borderwidth=2, fg="white", bg="black", command=lambda: clear())
clear_button.grid(row=1, column=1)
negative_button = Button(cal, text="+/-", width=4, height=2,borderwidth=2, fg="white", bg="black", command=lambda :press_negative())
negative_button.grid(row=1, column=2)
percent_button = Button(cal, text="%", width=4, height=2,borderwidth=2, fg="white", bg="black", command=lambda :press_percent())
percent_button.grid(row=1, column=3)
division = Button(cal, text="/", width=4, height=2,borderwidth=2, fg="white", bg="orange", command=lambda: press("/"))
division.grid(row=1, column=4)
number_9 = Button(cal, text="9", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(9))
number_9.grid(row=2, column=3)
number_8 = Button(cal, text="8", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(8))
number_8.grid(row=2, column=2)
number_7 = Button(cal, text="7", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(7))
number_7.grid(row=2, column=1)
number_6 = Button(cal, text="6", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(6))
number_6.grid(row=3, column=3)
number_5 = Button(cal, text="5", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(5))
number_5.grid(row=3, column=2)
number_4 = Button(cal, text="4", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(4))
number_4.grid(row=3, column=1)
number_3 = Button(cal, text="3", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(3))
number_3.grid(row=4, column=3)
number_2 = Button(cal, text="2", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(2))
number_2.grid(row=4, column=2)
number_1 = Button(cal, text="1", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(1))
number_1.grid(row=4, column=1)
number_0 = Button(cal, text="0", width=10, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press(0))
number_0.grid(row=5, columnspan=3)
dot = Button(cal, text=".", width=4, height=2,borderwidth=2, fg="white", bg="gray", command=lambda: press("."))
dot.grid(row=5, column=3)
multi = Button(cal, text="x", width=4, height=2,borderwidth=2, fg="white", bg="orange", command=lambda: press("*"))
multi.grid(row=2, column=4)
subtraction = Button(cal, text="-", width=4, height=2,borderwidth=2, fg="white", bg="orange", command=lambda: press("-"))
subtraction.grid(row=3, column=4)
plus = Button(cal, text="+", width=4, height=2,borderwidth=2, fg="white", bg="orange", command=lambda: press("+"))
plus.grid(row=4, column=4)
equal = Button(cal, text="=", width=4, height=2,borderwidth=2, fg="white", bg="orange",  command=lambda: press_equal())
equal.grid(row=5, column=4)

cal.mainloop()