import numpy as np


def transponMatrix(list_1):
    matrix = np.transpose(list_1)
    return matrix.tolist()


def multiplyM(list_1, list_2):
    return np.dot(list_1, list_2).tolist()



def addM(list_1, list_2):
    return np.add(list_1, list_2).tolist()


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Транспонированная матрица: ")
print(transponMatrix(list1))
print(" ")
print("Умножение матриц: ")
print(multiplyM(list1, list2))
print(" ")
print("Сложение матриц: ")
print(addM(list1, list2))
