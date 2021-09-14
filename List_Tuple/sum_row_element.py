#Hãy viết hàm sum_row_elements() nhận vào một Tuple hai chiều.
# Kết quả trả về là một Tuple một chiều với mỗi phần tử là tổng của các số trên cùng một cột.

#Create random matrix
import random

role = int(input("Please enter role and column:"))
column = int(input("Please enter column:"))

def matrix():
    matrix = []
    for i in range(role):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(0, 9))
    return matrix

#Define a function to merge 2-dimensional tuple
def sum_row_element(lst):
    raw_list = []
    length = len(lst[0])
    for i in range(length):
        sum = 0
        for j in range(len(lst)):
            sum += lst[j][i]
        raw_list.append(sum)
    return raw_list

#main
matrix = matrix()
tuple_matrix = tuple(matrix)
print("Your 2-dimensional matrix:\n", tuple_matrix)
flat_tuple = tuple(sum_row_element(matrix))
print("Your flat tuple:\n", flat_tuple)



