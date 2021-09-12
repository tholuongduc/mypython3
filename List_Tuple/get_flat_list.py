#Viết hàm get_flat_list() nhận đầu vào là một list 2 chiều. Đầu ra là list 1 chiều chứa tất cả phần tử của list đầu vào.
#Nếu index của hàng là số lẻ thì hãy đảo ngược vị trí các phần tử thuộc hàng đó.

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

#Define a function to merge 2-dimensional list
def get_flat_list(lst):
    flat_lst = []
    for i in range(len(lst)):
        if i % 2 != 0:
            lst[i].reverse()
            flat_lst += lst[i]
        else:
            flat_lst += lst[i]
    return flat_lst

#main
matrix = matrix()
print("Your 2-dimensional matrix:\n", matrix)
flat_list = get_flat_list(matrix)
print("Your flat list:\n", flat_list)

