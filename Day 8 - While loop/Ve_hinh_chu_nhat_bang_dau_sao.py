#Ve hinh chu nhat = dau *
dai = int(input("Nhap chieu dai:"))
cao = int(input("Nhap chieu cao:"))

i = 0
j = 0
print(dai * "* ")
while i < (cao - 2):
    print("*" + (2*dai -3) * " " + "*")
    i += 1
print(dai * "* ")