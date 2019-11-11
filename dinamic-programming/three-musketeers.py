# Do you know a story about the three musketeers? Anyway, you will learn about its origins now.

# Richelimakieu is a cardinal in the city of Bearis. He is tired of dealing with crime by himself. He needs three brave warriors to help him to fight against bad guys.

# There are n warriors. Richelimakieu wants to choose three of them to become musketeers but it's not that easy. The most important condition is that musketeers must know each other to cooperate efficiently. And they shouldn't be too well known because they could be betrayed by old friends. For each musketeer his recognition is the number of warriors he knows, excluding other two musketeers.

# Help Richelimakieu! Find if it is possible to choose three musketeers knowing each other, and what is minimum possible sum of their recognitions.

# Input
# The first line contains two space-separated integers, n and m (3 ≤ n ≤ 4000, 0 ≤ m ≤ 4000) — respectively number of warriors and number of pairs of warriors knowing each other.

# i-th of the following m lines contains two space-separated integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi). Warriors ai and bi know each other. Each pair of warriors will be listed at most once.

# Output
# If Richelimakieu can choose three musketeers, print the minimum possible sum of their recognitions. Otherwise, print "-1" (without the quotes).

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
            minRecog = min(recognitions[i] + recognitions[x] + recognitions[y], minRecog)

if minRecog == 9999999:
    print(-1)
else:
    print(minRecog - 6)