age = float(input("Nhap so tuoi cua ban:"))
weight = float(input("Nhap can nang cua ban:"))
height = float(input("Nhap chieu cao cua ban:"))

BMI = weight / (height * 2)
print("BMI cua ban la:" + str(BMI))

if age >= 20:
    if BMI > 40:
        print("Beo phi cap do III")
    elif BMI < 40 and BMI >= 35:
        print("Beo phi cao di II")
    elif BMI < 35 and BMI >= 30:
        print("Beo phi cap do I")
    elif BMI < 30 and BMI >= 25:
        print("Thua can")
    elif BMI < 25 and BMI >= 18.5:
        print("binh thuong")
    elif BMI < 18.5 and BMI >= 17:
        print("Gay cap do I")
    elif BMI < 17 and BMI <= 16:
        print("Gay cap do II")
    else:
        print("Gay cap do III")
else:
    print("Ban chua du 20 tuoi")