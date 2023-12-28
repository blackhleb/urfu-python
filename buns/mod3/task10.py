a = int(input())

matrix = []
newMatrix = []

for i in range(0, a):
    temp = []
    for j in range(0, a):
        temp.append(i + 1)
    matrix.append(temp)
    newMatrix.append(["0"] * a)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        newMatrix[j][i] = matrix[i][j]


def printMatrix(a):
    for i in a:
        print(*i)


printMatrix(newMatrix)
print()
printMatrix(matrix)



