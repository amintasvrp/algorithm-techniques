# Sereja has an array a, consisting of n integers a1, a2, ..., an. The boy cannot sit and do nothing, he decided to study an array. Sereja took a piece of paper and wrote out m integers l1, l2, ..., lm (1 ≤ li ≤ n). For each number li he wants to know how many distinct numbers are staying on the positions li, li + 1, ..., n. Formally, he want to find the number of distinct numbers among ali, ali + 1, ..., an.?

# Sereja wrote out the necessary array elements but the array was so large and the boy was so pressed for time. Help him, find the answer for the described question for each li.

# Input
# The first line contains two integers n and m (1 ≤ n, m ≤ 105). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105) — the array elements.

# Next m lines contain integers l1, l2, ..., lm. The i-th line contains integer li (1 ≤ li ≤ n).

# Output
# Print m lines — on the i-th line print the answer to the number li.


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