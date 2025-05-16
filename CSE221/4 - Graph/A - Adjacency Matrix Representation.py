nodes, edges = map(int, input().split())
adj_mat = [[0] * nodes for _ in range(nodes)]
for connections in range(edges):
    u, v, cost = map(int, input().split())
    adj_mat[u - 1][v - 1] = cost
for row in adj_mat:
    print(*row)
