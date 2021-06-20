import random
import time


def matrixCreation():
    
    matrix=[]
    col:int=random.randint(3, 5)
    row:int=random.randint(3, 5)
    print("Matrix is -")
    for row_index in range(row):
        rowlist=[]
        for col_index in range(col):
            rowlist.append(random.randint(1, 50))
        print(rowlist)
        matrix.append(rowlist)
    return matrix


def findInMatrix(matrix, X):

    present=0
    for row in matrix:
        if X in row:
            present=1
            break

X = random.randint(1, 50)
print("number to be searched is-",X)

matrix=matrixCreation()
present=findInMatrix(matrix, X)

if(present==1):
    print("number is present")
else:
    print("number is not present")