import turtle
pen = turtle.Turtle()
import Class_rectangle as cr
rectangle01 = cr.rectangle(long = 200,width= 300)
def show_menu():
    print('''Please select program mode:
        1) Show the rectangle information
        2) Draw the rectangle
        3) Set long, width
        4) Exit
          ''')
#Select program mode
def get_choice():
    return input("Please select mode: ")


#main
while True:
    show_menu()
    user_choice = get_choice()
    print("You select mode: " + user_choice)

    if user_choice == "4":
        break
    elif user_choice == "1":
        print(f'Rectangle Infor \n{rectangle01}')
    elif user_choice == "2":
        cr.rectangle.draw_rectangle(rectangle01, pen)
        turtle.done()
    elif user_choice == "3":
        long = int(input("Long: "))
        width = int(input("Width: "))
        cr.rectangle.set_long(rectangle01, long)
        cr.rectangle.set_long(rectangle01, width)
    else:
        print("Invalid mode! Try again!")

