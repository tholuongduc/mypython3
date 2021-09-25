#Define class
class rectangle:
    long = 0
    width = 0

    def __init__(self, long, width):
        self.long = long
        self.width = width

    def set_long(self, long):
        while True:
            try:
                if long <= 0:
                    print("Invalid!Input value should be higher than 0")
                else:
                    self.long = long
                    break
            except ValueError:
                print("Invalid!Input value should be higher than 0")
    def set_width(self, width):
        while True:
            try:
                if width <= 0:
                    print("Invalid!Input value should be higher than 0")
                else:
                    self.long = width
                    break
            except ValueError:
                print("Invalid!Input value should be higher than 0")

    #define square formula
    def square(self):
        square = self.long * self.width
        return square
    #define perimeter formula
    def perimeter(self):
        perimeter = (self.long + self.width) * 2
        return perimeter

    def draw_rectangle(self, pen):
        for i in range(2):
            pen.forward(self.long)
            pen.left(90)
            pen.forward(self.width)
            pen.left(90)

    def __str__(self):
        return f"Long:{self.long}\nWidth:{self.width}\n" \
        + f"Square: {self.square()}\n" \
        + f"Perimeter: {self.perimeter()}"




