dimension = int(input())
x, y = map(int, input().split())
kings_moves = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1))

possible_moves = []
for i in range(8):    
    ux, uy = x + kings_moves[i][0], y + kings_moves[i][1]
    if 0 <= ux - 1 < dimension and 0 <= uy - 1 < dimension:
        possible_moves.append((ux, uy))

possible_moves.sort()
print(len(possible_moves))
for move in possible_moves:
    print(move[0], move[1])
