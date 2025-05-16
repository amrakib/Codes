# Task 07: Game Arena
from demo import print_matrix
import numpy as np
def play_game(arena):
	row, col = arena.shape
	points = 0
	for i in range(row):
		for j in range(col):
			if arena[i][j] % 50 == 0 and arena[i][j] != 0:
				if i - 1 >= 0 and arena[i - 1][j] == 2:
					points += 2
				if i + 1 < row and arena[i + 1][j] == 2:
					points += 2
				if j - 1 >= 0 and arena[i][j - 1] == 2:
					points += 2
				if j + 1 < col and arena[i][j + 1] == 2:
					points += 2
	return f"Points Gained: {points}. Your team has survived the game." if points >= 10 else f"Points Gained: {points}. Your team is out."


arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
print(play_game(arena))
#This should print
#Points Gained: 6. Your team is out.

print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
print(play_game(arena))
#This should print
#Points Gained: 14. Your team has survived the game.