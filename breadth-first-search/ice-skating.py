n = int(input())
visited = [False] * 1001
nodes = []


def verify(i):
    visited[i] = True
    for j in range(n):
        if not visited[j] and (nodes[i][0] == nodes[j][0] or nodes[i][1] == nodes[j][1]):
            verify(j)


for i in range(n):
    cordinates = tuple(map(int, input().split()))
    nodes.append(cordinates)

drifts = 0
for i in range(n):
    if not visited[i]:
        verify(i)
        drifts += 1

print (drifts - 1)
