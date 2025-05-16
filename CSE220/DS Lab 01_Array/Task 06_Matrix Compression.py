# Task 07: Game Arena
from demo import print_matrix
import numpy as np
def compress_matrix(mat):
    row, col = mat.shape
    arr = np.zeros(((row // 2), (col // 2)), dtype=int)
    if (row and col) % 2 == 0:
      for i in range(0, row - 1, 2):
          for j in range(0, col - 1, 2):
              arr[i//2][j//2] = mat[i][j] + mat[i+1][j] + mat[i][j+1] + mat[i+1][j+1]
      return arr
    else: return "Invalid Matrix"

matrix = np.array([[1, 2, 3, 4, 1, 1],
                   [5, 6, 7, 8, 1, 1],
                   [1, 3, 5, 2, 1, 1],
                   [-2, 0, 6, -3, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1]
                   ])
print(matrix)
print("...............")
returned_array = compress_matrix(matrix)
print(returned_array)
# This should print

# |  14  |  22 |
# --------------
# |  2  |  10  |
# --------------