import random

role = int(input("Please enter role:"))
column = int(input("Please enter column"))

def matrix():
    matrix = []
    for i in range(role):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(0, 9))
    return matrix

matrix = matrix()
print(matrix)