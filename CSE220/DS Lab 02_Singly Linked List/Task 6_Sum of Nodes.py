from __Prerequisite__ import Node, createList
import fhm_unittest as unittest
import numpy as np


def sum_dist(head, arr):
    sum = 0
    for i in range(len(arr)):
        temp = head
        j = 0
        while temp != None:
            if j == arr[i]:
                sum += temp.elem
            temp = temp.next
            j += 1
    return sum


print('==============Test Case 1=============')
LL1 = createList(np.array([10, 16, -5, 9, 3, 4]))
dist = np.array([2, 0, 5, 2, 8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}')  # This should print Sum of Nodes: 4
unittest.output_test(returned_value, 4)
print()
