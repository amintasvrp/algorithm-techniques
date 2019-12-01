n, m = map(int, raw_input().split())
nextN = n + 1
nextM = m + 1
knowns = [[False] * (nextN) for i in range(nextN)]
recognitions = [0] * (nextN)
a = [0] * (nextM)
b = [0] * (nextM)
minRecog = 9999999

for i in xrange(m):
    x, y = map(int, raw_input().split())
    a[i] = x
    b[i] = y
    knowns[x][y] = True
    knowns[y][x] = True
    recognitions[x] += 1
    recognitions[y] += 1

for i in xrange(1, nextN):
    for j in xrange(1, nextM):
        x = a[j]
        y = b[j]
        if(knowns[i][x] and knowns[i][y]):
            minRecog = min(
                recognitions[i] + recognitions[x] + recognitions[y], minRecog)

if minRecog == 9999999:
    print(-1)
else:
    print(minRecog - 6)
