import sys
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (N + 1)
color = [0] * (N + 1)


def BFS(G, s, visited, color):
    q = deque()
    q.append(s)
    visited[s] = True
    count = [1, 0]
    while len(q) > 0:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                color[w] = 1 - color[v]
                count[color[w]] += 1
                q.append(w)
            elif color[v] == color[w]:
                return (0, 0)
    return count

players = 0
for k in range(1, N + 1):
    if not visited[k]:
        i, j = BFS(graph, k, visited, color)
        players += max(i, j)

print(players)
