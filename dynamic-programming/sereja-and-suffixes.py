n, m = map(int, input().split())
a = list(map(int, input().split()))

remains = 0
numbers = [0] * n
distinctNumbers = [0] * ((10 ** 5)+1)

for i in range(n-1, -1, -1):
    if distinctNumbers[a[i]] == 0:
        remains += 1
        distinctNumbers[a[i]] = 1
    numbers[i] = remains

for i in range(m):
    key = int(input())
    print (numbers[key-1])
