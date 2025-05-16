import sys
sys.setrecursionlimit(2 * 10**5)
input = sys.stdin.readline

city_count, road_count = map(int, input().split())

routes = []
for _ in range(road_count):
    start, end, cost = map(int, input().split())
    routes.append((cost, start, end))

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_b] = root_a
        return True

routes.sort()

uf = UnionFind(city_count)
minimum_total_cost = 0

for cost, node_a, node_b in routes:
    if uf.union(node_a, node_b):
        minimum_total_cost += cost

print(minimum_total_cost)
