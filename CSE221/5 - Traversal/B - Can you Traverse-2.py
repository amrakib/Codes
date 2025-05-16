import sys
from collections import defaultdict

sys.setrecursionlimit(2 * 100000 + 50)
cities, roads = map(int, sys.stdin.readline().split())
u = tuple(map(int, sys.stdin.readline().split()))
v = tuple(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for i in range(roads):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

visited = {i: "w" for i in range(1, cities + 1)}

for adj in graph:
    graph[adj].sort()

def DFS(v):
    visited[v] = "g"
    print(v, end=" ")
    for w in graph[v]:
        if visited[w] == "w":
            DFS(w)

DFS(1)
