month = int(input("Nhap thang:"))
year = int(input("Nhap nam:"))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Thang nay co 31 ngay")
elif month  == 2:
    if year % 4 == 0:
        print("Thang nay co 29 ngay")
    else:
        print("Thang nay co 28 ngay")
else:
    print("Thang nay co 30 ngay")