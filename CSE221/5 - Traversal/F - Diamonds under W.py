import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
arr = [list(input()) for _ in range(R)]
moves = ((0, 1), (1, 0), (-1, 0), (0, -1))


def collect():
    max_d = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] in (".", "D"):
                diamond = BFS(i, j)
                max_d = max(max_d, diamond)
    return max_d


def BFS(r, c):
    count = 0 if arr[r][c] != "D" else 1
    q = deque()
    q.append((r, c))
    arr[r][c] = None
    while len(q) != 0:
        x, y = q.popleft()
        for dx, dy in moves:
            ux, uy = x + dx, y + dy
            if 0 <= ux < R and 0 <= uy < C and arr[ux][uy] in (".", "D"):
                if arr[ux][uy] == "D":
                    count += 1
                arr[ux][uy] = None
                q.append((ux, uy))
    return count


print(collect())
