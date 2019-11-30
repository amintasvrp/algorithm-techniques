from heapq import heappush, heappop
 
n, m = map(int, raw_input().split())

graph = []
for i in xrange(n+1):
    graph.append([])
 
for _ in xrange(m):
    begin, end, cost = map(int, raw_input().split())
    graph[begin].append((end, cost))
    graph[end].append((begin, cost))

heap = [(0,1)]
lower_costs = [float("inf")] * (n + 1)
parent = [0] * (n + 1)
 
while heap:
    accumulated_cost, begin = heappop(heap)
    for end, current_cost in graph[begin]:
        current_cost += accumulated_cost
        if lower_costs[end] > current_cost:
            parent[end] = begin
            lower_costs[end] = current_cost
            heappush(heap, (current_cost, end))
 
if(not parent[n]):
    print (-1)
else:
    path = [n]
    while n != 1:
        n = parent[n]
        path.append(n)
 
    path.reverse()
    
 
    print(' '.join(map(str, path)))