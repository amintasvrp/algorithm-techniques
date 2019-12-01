import sys


def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("-----------------")


m, n = map(int, input().split())
matrix = [[] * n for i in range(m)]

for i in range(m):
    matrix[i] = list(map(int, input().split()))
    printMatrix(matrix)

for i in range(1, m):
    matrix[i][0] += matrix[i-1][0]
    printMatrix(matrix)

for i in range(1, n):
    matrix[0][i] += matrix[0][i-1]
    printMatrix(matrix)

for i in range(1, m):
    for j in range(1, n):
        matrix[i][j] += max(matrix[i-1][j], matrix[i][j-1])
        printMatrix(matrix)

for i in range(m):
    sys.stdout.write(str(matrix[i][n-1])+" ")
