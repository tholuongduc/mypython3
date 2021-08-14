money = int(input("Nhap so tien da mua:"))

if money >= 150:
    print("So tien phai tra:" + str(money - 15))
elif money >= 100 and money < 150:
    print("So tien phai tra:" + str(money - 25))
elif money >= 150:
    print("So tien phai tra:" + str(money - 50))
else:
    print("so tien phai tra:" + str(money))