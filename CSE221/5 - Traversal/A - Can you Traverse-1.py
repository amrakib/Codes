from collections import deque


class Queue:
    def __init__(self):
        self.tbv = deque()

    def enqueue(self, node):
        self.tbv.append(node)

    def dequeue(self):
        return self.tbv.popleft()

    def is_empty(self):
        return len(self.tbv) == 0


def BFS(G, s):
    q = Queue()
    color[s] = "g"
    q.enqueue(s)
    while not q.is_empty():
        v = q.dequeue()
        print(v, end=" ")
        for w in G[v]:
            if color[w] == "w":
                color[w] = "g"
                q.enqueue(w)
    

graph = {}
cities, roads = map(int, input().split())
color = {i: "w" for i in range(1, cities + 1)}
for i in range(roads):
    u, v = map(int, input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

for node in graph:
    graph[node].sort()

BFS(graph, 1)