n = int(input())
data = [[0] * (n+1) for i in range(n+1)]
ans = [0] * (n+1)

for i in xrange(1, n+1):
    data[i] = [0] + map(int, raw_input().split())
    ans[0] += sum(data[i])

deleting = (map(int, raw_input().split())) + [0]
deleting.reverse()

f = [False] * (n+1)

for x in xrange(1, n+1):
    ans[x] = 0
    k = deleting[x]
    f[k] = True
    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])
            if (f[i] and f[j]):
                ans[x] += data[i][j]

ans.pop(0)
ans.reverse()
print(' '.join(map(str, ans)))
