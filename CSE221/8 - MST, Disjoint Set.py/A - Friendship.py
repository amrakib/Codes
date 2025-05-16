import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**18)
n, k = map(int, input().split())
parent = list(range(n + 1))
group_size = [1] * (n + 1)
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]
def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        if group_size[root_u] < group_size[root_v]:
            root_u, root_v = root_v, root_u
        parent[root_v] = root_u
        group_size[root_u] += group_size[root_v]
        group_size[root_v] = 0
    return group_size[root_u]
for k in range(k):
    a, b = map(int, input().split())
    print(union(a, b))
