from tkinter import *

win = Tk()
win.title("Grid")

for i in range(10):
    for j in range(10):
        color = "yellow"
        if (i+j) % 2 == 0:
            color = "green"
        lable = Label(win, text="", width=4, height=2, background=color)
        lable.grid(row=i, column=j)

win.mainloop()

