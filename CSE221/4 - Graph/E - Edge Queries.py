vertices, connections = map(int, input().split())
source = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
in_degree = [0] * vertices
out_degree = [0] * vertices

for i in range(connections):
    in_degree[end[i] - 1] += 1
    out_degree[source[i] - 1] += 1

for j in range(vertices):
    print(in_degree[j] - out_degree[j], end=" ")
    