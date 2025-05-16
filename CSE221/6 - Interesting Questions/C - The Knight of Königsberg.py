from collections import deque
N = int(input())
ix, iy, fx, fy = map(int, input().split())
count = -1

moves = [(-1, 2), (1, 2), (2, 1), (2, -1), 
            (1, -2), (-1, -2), (-2, -1), (-2, 1)]

visited = [[0] * (N + 1) for _ in range(N + 1)]
q = deque()
q.append((ix, iy, 0))
visited[ix][iy] = 1

while len(q) > 0:
    x, y, d = q.popleft()
    if x == fx and y == fy:
        count = d
        break
    for dx, dy in moves:
        mx, my = x + dx, y + dy
        if 1 <= mx <= N and 1 <= my <= N and not visited[mx][my]:
            visited[mx][my] = 1
            q.append((mx, my, d + 1))

print(count)