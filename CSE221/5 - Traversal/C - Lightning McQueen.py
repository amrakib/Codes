import sys
from collections import defaultdict, deque

N, M, S, D = map(int, sys.stdin.readline().split())
u = tuple(map(int, sys.stdin.readline().split()))
v = tuple(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for i in range(M):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])


for node in graph:
    graph[node].sort()


color = [False] * (N + 1)
distance = [-1] * (N + 1)
parent = [-1] * (N + 1)


def bfs_shortest_path(G, s, t):
    q = deque()
    q.append(s)
    color[s] = True
    distance[s] = 0
    while len(q) != 0:
        node = q.popleft()
        for w in G[node]:
            if not color[w]:
                q.append(w)
                color[w] = True
                parent[w] = node
                distance[w] = distance[node] + 1

bfs_shortest_path(graph, S, D)

if not color[D]:
    print(-1)
else:
    path = []
    curr = D
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(len(path) - 1)
    print(*path)