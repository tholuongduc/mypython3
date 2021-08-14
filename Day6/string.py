# Khai báo chuỗi string
my_string = "Python programming language"
print("Độ dài chuỗi =", len(my_string))

# Hàm count - trả về số lần chuỗi con có mặt trong chuỗi
my_string2 = "Python programming language and PHP programming language"
print("Số lần từ 'language' xuất hiện trong chuỗi =", my_string2.count('language'))

# Hàm lower() - chuyển chuỗi về dạng in thường
print("Chuỗi in thường", my_string.lower())
# Hàm upper() - chuyển chuỗi về dạng in hoa
print("Chuỗi in thường", my_string.upper())

# Hàm lstrip - loại bỏ các kí tự trắng ở đầu chuỗi
my_string3 = "   Python programming language   "
print("Chuỗi sau khi loại bỏ kí tự trắng ở đầu '{}'".format(my_string3.lstrip()))

# Hàm rstrip - loại bỏ các kí tự trắng ở cuối chuỗi
print("Chuỗi sau khi loại bỏ kí tự trắng ở cuối '{}'".format(my_string3.rstrip()))
# Hàm rstrip - loại bỏ các kí tự trắng ở đầu và cuối chuỗi
print("Chuỗi sau khi loại bỏ kí tự trắng ở đầu và cuối chuỗi '{}'".format(my_string3.strip()))

# Hàm split - chia chuỗi
my_string = "Python programming language"
print("Chuỗi sau khi chia = ",my_string.split(' '))

print("This is \x61 good example")
print(r"This is \x61 \ngood example")