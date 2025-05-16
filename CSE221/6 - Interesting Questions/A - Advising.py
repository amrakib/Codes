import sys
from collections import defaultdict, deque
N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
in_degree = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    in_degree[v] += 1

def kahn_toposort(G, N, in_deg):
    result = []
    q = deque()
    for i in range(1, N + 1):
        if in_deg[i] == 0:
            q.append(i)
    while len(q) > 0:
        node = q.popleft()
        result.append(node)
        for v in G[node]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
    
    print(*result) if len(result) == N else print(-1)

kahn_toposort(graph, N, in_degree)