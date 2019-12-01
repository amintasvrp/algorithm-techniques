def matrix(packages, maxTime):
    amount = [x[1] for x in packages]
    time = [x[0] for x in packages]
    matrix = [[0] * (maxTime+1) for i in range(len(amount)+1)]
    for i in range(1, len(amount)+1):
        for j in range(1, maxTime + 1):
            if(j < amount[i-1]):
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], time[i-1] +
                                   matrix[i-1][j-amount[i-1]])

    return matrix


def minutes(packages, maxTime):
    packages = sorted(packages, key=lambda element: (
        element[1], element[0]), reverse=True)
    result = matrix(packages, maxTime)
    return result[-1][-1]


def pizzas(packages, maxTime):
    packages = sorted(packages, key=lambda element: (
        element[1], element[0]), reverse=True)
    amount = [x[1] for x in packages]
    time = [x[0] for x in packages]

    matrixMinutes = matrix(packages, maxTime)
    i = len(matrixMinutes) - 1
    j = len(matrixMinutes[0]) - 1
    packages = []

    while(matrixMinutes[i][j] != 0):
        if(matrixMinutes[i][j] == matrixMinutes[i-1][j]):
            i = i - 1
        else:
            packages.append((time[i-1], amount[i-1]))
            j = j - amount[i-1]
            i = i - 1

    return packages


packages = [(14, 4), (21, 2), (26, 7), (18, 4), (30, 13), (10, 2)]
n = 7
print(pizzas(packages, n))
print(minutes(packages, n))
