# Dada a lista de adjacência de um grafo direcionado, escreva uma função que
# retorna a ordem topológica do mesmo, recebendo também como parâmetro a raiz
# do grafo.

def topological_order(adj, root):
    visited = {}
    for i in adj.keys():
        visited[i] = False
    
    result = dfs(root, adj, visited)
    for node in visited.keys():
        if(not visited[node]):
            result = dfs(node, adj, visited) + result
    return result

def dfs(node, adj, visited):
    if(visited[node]):
        return []
    visited[node] = True
    result = []
    for child in adj[node]:
        result = dfs(child, adj, visited) + result
    result = [node] + result
    return result

print(topological_order({'s': ['w'], 'r': ['s', 'v'], 't': ['w', 'x'], 'w': [], 'v': ['w', 's'], 'x': []}, 'r'))