#Task 05: Row Rotation Policy of BRACU Classroom
from demo import print_matrix
import numpy as np
def row_rotation(exam_week, seat_status):
    row, col = seat_status.shape
    for repeat in range(exam_week - 1):
        for j in range(col):
            temp = seat_status[row - 1][j]
            for i in range(row - 1, 0, -1):
                seat_status[i][j] = seat_status[i-1][j]
            seat_status[0][j] = temp
    print_matrix(seat_status)
    for i in range(row):
        for j in range(col):
            if seat_status[i][j] == "AA":
                spot = i+1
                return spot


seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                        [ 'F' , 'G' , 'H' , 'I' , 'J'],
                        [ 'K' , 'L' , 'M' , 'N' , 'O'],
                        [ 'P' , 'Q' , 'R' , 'S' , 'T'],
                        [ 'U' , 'V' , 'W' , 'X' , 'Y'],
                        [ 'Z' , 'AA', 'BB', 'CC','DD']])
exam_week=3
print_matrix(seat_status)
print()
row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2