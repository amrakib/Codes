from __Prerequisite__ import createList, printLinkedList
import fhm_unittest as unittest
import numpy as np


def check_similar(building_1, building_2):
    b1 = building_1
    b2 = building_2
    flag = True
    while b1 != None and b2 != None:
        if b1.elem != b2.elem:
            flag = False
            break
        b1, b2 = b1.next, b2.next
    return "Similar" if flag and b1 == b2 else "Not Similar"


print('==============Test Case 1=============')
building_1 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end=' ')
printLinkedList(building_1)
print('Building 2: ', end=' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Similar'
unittest.output_test(returned_value, 'Similar')
print()

print('==============Test Case 2=============')
building_1 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
building_2 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end=' ')
printLinkedList(building_1)
print('Building 2: ', end=' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 3=============')
building_1 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
print('Building 1: ', end=' ')
printLinkedList(building_1)
print('Building 2: ', end=' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 4=============')
building_1 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
building_2 = createList(
    np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end=' ')
printLinkedList(building_1)
print('Building 2: ', end=' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()
