#Task 04: Zigzag Walk
from demo import print_matrix
import numpy as np
def walk_zigzag(floor):
    flag = True
    i = 0
    final = floor.shape[0] - 1
    for j in range(floor.shape[1]):
        while i < (floor.shape[0]) and i >= 0:
            if flag:
                print(floor[i][j], end=" ")
                i += 2
            else:
                print(floor[i][j], end=" ")
                i -= 2
        print()
        flag = False if flag else True
        if flag:
            i = 0
        elif i == floor.shape[0] + 1:
            i = floor.shape[0] - 2
        else:
            i = floor.shape[0] - 1



floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8