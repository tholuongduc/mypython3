from tkinter import *
from tkinter.ttk import *

def BMI_Calculate():
    my_weight = weight.get()
    my_height = height.get()
    BMI = float(my_weight) / (float(my_height) ** 2)
    result.config(text=BMI)
    if BMI > 40:
        description = "Béo phì cấp độ III"
        result_bmi_description.config(text=description)
    elif BMI < 40 and BMI >= 35:
        description = "Béo phì cấp độ II"
        result_bmi_description.config(text=description)
    elif BMI < 35 and BMI >= 30:
        description = "Béo phì cấp độ I"
        result_bmi_description.config(text=description)
    elif BMI < 30 and BMI >= 25:
        description = "Thừa cân"
        result_bmi_description.config(text=description)
    elif BMI < 25 and BMI >= 18.5:
        description = "Bình thường"
        result_bmi_description.config(text=description)
    elif BMI < 18.5 and BMI >= 17:
        description = "Gầy cấp độ I"
        result_bmi_description.config(text=description)
    elif BMI < 17 and BMI <= 16:
        description = "Gầy cấp độ II"
        result_bmi_description.config(text=description)
    else:
        description = "Gầy cấp độ III"
        result_bmi_description.config(text=description)

#create main windows
windows = Tk()
windows.title("BMI Calculator!")
app_lable = Label(windows,text="BMI CALCULATOR")
app_lable.pack()
#Create frame for weight
weight_frame = Frame(master=windows)
weight_frame.pack()
weight = Entry(weight_frame, width=10)
lable_weight = Label(master=weight_frame, text="Weight:")
weight.grid(row=0, column=1,sticky=W)
lable_weight.grid(row=0, column=0, sticky=E)

#Create frame for height
height_frame = Frame(master=windows)
height_frame.pack()
height = Entry(height_frame, width=10)
lable_height = Label(master=height_frame, text="Height:")
height.grid(row=1, column=1)
lable_height.grid(row=1, column=0)

#Create button
button1 = Button(master=windows, text="Calculate BMI", command=BMI_Calculate)
button1.pack()

#Create frame for result
fr_bmi_result = Frame(master=windows)
fr_bmi_result.pack()
lable_result = Label(master=fr_bmi_result, text="BMI Result:")
result = Label(master=fr_bmi_result)
lable_result.grid(row=2, column=0)
result.grid(row=2, column=1)

#Create frame for description
fr_bmi_description = Frame(windows)
fr_bmi_description.pack()
lb_bmi_description = Label(fr_bmi_description, text="Description:")
result_bmi_description = Label(fr_bmi_description)
lb_bmi_description.grid(row=3, column=0)
result_bmi_description.grid(row=3, column=1)


windows.mainloop()
