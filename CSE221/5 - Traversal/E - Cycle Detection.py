import sys
sys.setrecursionlimit(2 * 100000 + 50)
N, M = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

def dfs_check(node, G, visited, path):
    visited[node] = True
    path[node] = True
    for neighbor in G[node]:
        if not visited[neighbor]:
            if dfs_check(neighbor, G, visited, path):
                return True
        elif path[neighbor]:
            return True
    path[node] = False
    return False

def cyclic(G, N):
    visited = [False] * (N + 1)
    path = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            if dfs_check(i, G, visited, path):
                return "YES"
    return "NO"

print(cyclic(graph, N))
