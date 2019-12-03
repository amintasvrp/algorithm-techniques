m, n = map(int, raw_input().split())
amount = 0
edges = []
vertices = []


def find_set(n):
    if vertices[n] != n:
        vertices[n] = find_set(vertices[n])
    return vertices[n]


def union_set(x, y, p):
    vertice1 = find_set(x)
    vertice2 = find_set(y)
    if vertice1 != vertice2:
        global amount
        amount -= edges[p][0]
        if vertice1 > vertice2:
            vertices[vertice1] = vertice2
        else:
            vertices[vertice2] = vertice1

while(True):
    params = map(int, raw_input().split())
    if params[0] == 0 and params[1] == 0: 
        break
    else:
        x = params[0]
        y = params[1]
        z = params[2]
        edges.append((z, x, y))
        amount += z

vertices = range(m+1)

edges.sort()

for i in xrange(n):
    union_set(edges[i][1], edges[i][2], i)

print(amount)
