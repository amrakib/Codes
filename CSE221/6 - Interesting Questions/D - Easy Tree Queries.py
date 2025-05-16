import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
N, R = map(int, sys.stdin.readline().split())
tree = defaultdict(list)
visited = [0] * (N + 1)
vertex_subtree_size = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def DFS(v):
    visited[v] = 1
    size = 1
    for w in tree[v]:
        if visited[w] == 0:
            size += DFS(w)
    vertex_subtree_size[v] = size
    return size


DFS(R)
queries = int(input())
for _ in range(queries):
    X = int(input())
    print(vertex_subtree_size[X])