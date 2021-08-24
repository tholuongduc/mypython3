#Viết chương trình xác định số KB mà file chiếm trên đĩa từ trong hệ thống NTFS
#Note: Trong hệ thống NTFS, bộ nhớ phân phối cho các file theo đơn vị cluster, mỗi cluster là 4KB (tức là 4096 byte). Như vậy dù file của bạn có kích thước là 1 byte nó vẫn chiếm bộ nhớ 4KB trên ổ đĩa.

import math

n = int(input("Hãy nhập kích thước file trong đơn vị byte (n là số nguyên dương):"))

a = n // 4096
b = n % 4096
#C1:Su dung If-else:
#kb = 0
#if b == 0:
#    kb = a * 4
#else:
#    kb = (a+1)*4
#print("Dung lượng file chiếm là: ", kb, "KB")

#C2:Su dung toan tu 3 ngoi
kb = (a * 4) if (n % 4096 == 0) else (a+1)*4
print("Dung lượng file chiếm là: ", kb, "KB")
