N = int(input())
words = [input() for _ in range(N)]

graph = {}
all_char = set()
for word in words:
    for c in word:
        graph.setdefault(c, set())
        all_char.add(c)

visited = {}
path = []

def graph_building(graph, N):
    for i in range(N - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1.startswith(w2):
            return True
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break
    return False


def topo_sort(graph, visited, root, stack):
    visited[root] = -1
    for neighbor in sorted(graph[root]):
        if neighbor not in visited:
            if topo_sort(graph, visited, neighbor, stack):
                return True
        elif visited[neighbor] == -1:
            return True
    visited[root] = 1
    stack.append(root)
    return False

def main():
    if graph_building(graph, N):
        return True
    for node in sorted(all_char, reverse=True):
        if node not in visited:
            if topo_sort(graph, visited, node, path):
                return True
    return False

has_error = main()

if has_error:
    print(-1)
else:
    print("".join(reversed(path)))
