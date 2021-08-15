import turtle
conditionShape = False

while (conditionShape == False):
    shapeInput = input("circle or square, please select:")
    if shapeInput in ['circle', 'square']:
        conditionShape = True
        conditionColor = False
        while (conditionColor == False):
            colorInput = input("What color do you want? yellow, red or blue:")
            if colorInput in ['yellow', 'red', 'blue']:
                conditionColor = True
                turtle.bgcolor("pink")
                turtle.title("Your shape!")
                displayShape = turtle.Turtle()
                displayShape.shapesize(10)
                displayShape.shape(shapeInput)
                displayShape.color(colorInput)
                turtle.done()
            else:
                print("Sorry!We don't have " + colorInput + ".Please select again:")
                conditionColor = False
    else:
        print("We don't have " + shapeInput + ".Please select again:")
        conditionShape = False

