import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def farthest(G, N, s):
    vis_dis = [-1] * (N + 1)
    q = deque()
    q.append(s)
    vis_dis[s] = 0
    farthest = s
    while len(q) > 0:
        v = q.popleft()
        for w in G[v]:
            if vis_dis[w] == -1:
                vis_dis[w] = vis_dis[v] + 1
                q.append(w)
                if vis_dis[w] > vis_dis[farthest]:
                    farthest = w
    return farthest, vis_dis[farthest]

u, _ = farthest(graph, N, 1)
v, d = farthest(graph, N, u)
print(d)
print(u, v)