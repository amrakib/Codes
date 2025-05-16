#Task 03: Decryption Process
import numpy as np
def decrypt_matrix(matrix):
    arr = np.zeros(matrix.shape[1] - 1)
    for i in range(matrix.shape[1] - 1):
        for j in range(matrix.shape[0]):
            arr[i] += (matrix[j][i+1] - matrix[j][i])
    return arr


matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]