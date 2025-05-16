vertices = int(input())
adj_mat = [[0] * vertices for _ in range(vertices)]

for i in range(vertices):
    links = tuple(map(int, input().split()))
    if links[0] > 0:
        for j in range(1, len(links)):
            adj_mat[i][links[j]] = 1

for row in adj_mat:
    print(*row)