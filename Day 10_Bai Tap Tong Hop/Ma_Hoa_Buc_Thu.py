import random
def reverse_string(content, key):
    key = int(key)
    sb = str(content[0:key])
    se = str(content[key:length_s])
    bs = sb[::-1]
    es = se[::-1]
    Q = bs + es
    return Q

#Nhập đoạn văn bản

s = input("Hãy nhập đoạn văn bản của bạn:")
length_s = len(s)
#key = input("Hãy nhập key:")
#Bạn muốn mã hóa hay giải mã? Mã hóa = 0, Giải mã = 1
mode = input("Bạn muốn mã hóa hay giải mã? Mã hóa chọn 0, Giải mã chọn 1:")

if mode == '0':
#    while True:
#        if key.isdigit() and int(key) <= length_s:
#            print("Bạn đã chọn chức năng mã hóa. Đang mã hóa văn bản, xin vui lòng đợi trong giây lát!")
#            break
#        else:
#            print("Key không hợp lệ!")
#            key = input("Hãy nhập số nguyên từ 1 đến " + str(length_s) + ":")
#            continue
    key = random.randint(1,length_s)
    Q = reverse_string(s, key)
    print("Đã mã hóa thành công! Đoạn văn bản được mã hóa là:\n" + Q)
    print("Key de giai ma la:", key)
elif mode == '1':
    key = input("Hay nhap key de giai ma:")
    print("Bạn đã chọn chức năng giải mã. Đang giải mã văn bản, xin vui lòng đợi trong giây lát!")
    Q = reverse_string(s, key)
    print("Đã giải mã thành công! Đoạn văn bản gốc là:\n" + Q)
else:
    print("Bạn chưa chọn đúng chức năng. Hãy chọn lại!")








