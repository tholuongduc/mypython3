from tkinter import *
from tkinter.ttk import *

login_windows = Tk()
login_windows.title("Login")
login_windows.geometry("400x250")
login_windows.resizable(False, False)


lable1 = Label(login_windows, text="Username")
lable1.place(x=30, y=30)
username = Entry(login_windows)
username.place(x=120, y=30)

lable2 = Label(login_windows, text="Password")
lable2.place(x=30, y=60)
password = Entry(login_windows)
password.place(x=120, y=60)

lable3 = Label(login_windows, text="Email")
lable3.place(x=30, y=90)
email = Entry(login_windows)
email.place(x=120, y=90)

login_windows.mainloop()