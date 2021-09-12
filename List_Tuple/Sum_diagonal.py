#Viết hàm sum_diagonal() tính tổng đường chéo chính của một ma trận vuông (là List 2 chiều có số hàng và cột bằng nhau).

#Create matrix
import random

role = int(input("Please enter role and column:"))
column = role

def matrix():
    matrix = []
    for i in range(role):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(0, 9))
    return matrix



#Define function to sum the number on diagonal of matrix
def sum_diagonal(matrix):
    sum_diagonal = 0
    for i in range(len(matrix)):
        sum_diagonal += matrix[i][i]
    return sum_diagonal

#main
matrix = matrix()
print("Your 2-dimensional matrix:\n", matrix)
sum_diagonal = sum_diagonal(matrix)
print("Sum of all number on diagonal of matrix:\n", sum_diagonal)