import sys
from collections import deque


N, M, S, D, K = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

for node in graph:
    graph[node].sort()


def bfs_shortest_path(G, s, t):
    color = [False] * (N + 1)
    parent = [-1] * (N + 1)
    q = deque()
    q.append(s)
    color[s] = True

    while q:
        node = q.popleft()
        if node == t:
            break
        for w in G[node]:
            if not color[w]:
                color[w] = True
                parent[w] = node
                q.append(w)


    if not color[t]:
        return None
    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


path1 = bfs_shortest_path(graph, S, K)
path2 = bfs_shortest_path(graph, K, D)

if not path1 or not path2:
    print(-1)
else:
    final_path = path1 + path2[1:]
    print(len(final_path) - 1)
    print(*final_path)