money = int(input("Nhap so tien da mua:"))

if money >= 150:
    print("So tien phai tra:" + str(money - 50))
elif money >= 100:
    print("So tien phai tra:" + str(money - 25))
elif money >= 75:
    print("So tien phai tra:" + str(money - 15))
else:
    print("so tien phai tra:" + str(money))