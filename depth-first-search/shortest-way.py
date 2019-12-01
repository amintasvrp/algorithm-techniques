WHITE = 0
GREY = 1


def sizeSmallestWay(v1, v2, adjacencyList):
    colors = [WHITE] * (len(adjacencyList) + 1)
    return sizeSmallestWayDFS(v1, v2, adjacencyList, colors)


def sizeSmallestWayDFS(v1, v2, adjacencyList, colors):
    colors[v1] = GREY
    if(v1 == v2):
        return 0
    else:
        minDistance = 9999999
        colorsCopy = colors.copy()
        for v in adjacencyList[v1-1]:
            if(colors[v] != GREY):
                distance = sizeSmallestWayDFS(v, v2, adjacencyList, colorsCopy)
                if(distance < minDistance):
                    minDistance = distance
        return 1 + minDistance


v1 = 4
v2 = 5
adjacencyList = [[2, 6], [1, 3, 4], [2, 4, 5], [2, 3, 7], [3], [1, 7], [6, 4]]
print(sizeSmallestWay(v1, v2, adjacencyList))
