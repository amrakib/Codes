def euclids_gcd(i, j):
    if j == 0: return i
    while j != 0:
        rem = i % j
        i = j
        j = rem
    return i

vertices, queries = map(int, input().split())
graph = [0] * (vertices + 1)
for source in range(1, vertices + 1):
    links = []
    for end in range(1, vertices + 1):
        if euclids_gcd(source, end) == 1 and source != end:
            links.append(end)
    graph[source] = links


for _ in range(queries):
    x, k = map(int, input().split())
    if len(graph[x]) < k:
        print(-1)
        continue
    print(graph[x][k - 1])
