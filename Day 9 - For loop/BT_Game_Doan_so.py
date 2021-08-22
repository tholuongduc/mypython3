#Xay dung tro choi doan so
import random
b = random.randint(1, 10)
print(b)
for i in range(3):
    a = int(input("Hãy nhập số nguyên từ 1 đến 10:"))
    print("Số của bạn đã chọn là: " + str(a))
    if a == b:
        print("Chính xác!")
        break
    else:
        print("Bạn đã dự đoán sai! Hãy nhập lại.")
        continue
else:
    print("Xin lỗi! Bạn đã hết lượt chơi.")
    print("Số ngẫu nhiên là: " + str(b))