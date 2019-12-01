def matrix(conj, sum):
    conj.append(0)
    conj = sorted(conj)

    matrix = []
    for x in range(len(conj)):
        matrix.append([])

    for i in range(len(conj)):
        matrix[i].append(0)

    for j in range(sum):
        matrix[0].append(0)

    for i in range(1, len(conj)):
        for j in range(1, sum + 1):
            if(conj[i] > j):
                matrix[i].append(matrix[i-1][j])
            else:
                matrix[i].append(
                    max(matrix[i-1][j], conj[i] + matrix[i-1][j-(conj[i])]))

    return matrix


def temSubconj(conj, sum):
    result = matrix(conj, sum)
    return result[-1][-1] == sum


def subconj(matrix, conj):
    i = len(matrix) - 1
    j = len(matrix[-1]) - 1
    conj = sorted(conj)

    subconj = []

    while(matrix[i][j] != 0):
        if(matrix[i][j] == matrix[i-1][j]):
            i -= 1
        else:
            subconj.append(conj[i])
            j = j - conj[i]
            i = i - 1

    return subconj


print(temSubconj([3, 34, 4, 12, 5, 2], 9))
m = matrix([3, 34, 4, 12, 5, 2], 9)
print(subconj(m, [3, 34, 4, 12, 5, 2]))
print(temSubconj([8, 34, 4, 12, 5, 1], 7))
