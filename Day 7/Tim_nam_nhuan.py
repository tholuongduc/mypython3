condition = False
while (condition == False):
    year = int(input("Hay nhap nam:"))
    i = year % 4
    j = year % 100
    k = year % 400
    if year > 0:
        condition = True
        if k == 0:
            print("Nam " + str(year) + " la nam nhuan")
        elif i == 0 and j != 0:
            print("Nam " + str(year) + " la nam nhuan")
        else:
            print("Nam " + str(year) + " khong la nam nhuan")
    else:
        print(str(year) + " khong dung. Vui long nhap so nguyen duong")
        condition = False