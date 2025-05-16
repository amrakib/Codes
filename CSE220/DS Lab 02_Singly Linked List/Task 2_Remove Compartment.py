from __Prerequisite__ import createList, printLinkedList
import numpy as np


def remove_compartment(head, n):
    temp = head
    index = 0
    while temp != None:
        index += 1
        temp = temp.next
    temp = head
    prev = None
    newHead = head
    if n > index or n == 0:
        return newHead
    while temp != None:
        if index == n:
            if prev != None:
                prev.next = temp.next
            else:
                newHead = head.next
            return newHead
        else:
            prev = temp
            temp = temp.next
            index -= 1


print('==============Test Case 1=============')
head = createList(np.array([10, 15, 34, 41, 56, 72]))
print('Original Compartment Sequence: ', end=' ')
printLinkedList(head)
head = remove_compartment(head, 2)
print('Changed Compartment Sequence: ', end=' ')
printLinkedList(head)  # This should print 10-->15-->34-->41-->72
print()
print('==============Test Case 2=============')
head = createList(np.array([10, 15, 34, 41, 56, 72]))
print('Original Compartment Sequence: ', end=' ')
printLinkedList(head)
head = remove_compartment(head, 7)
print('Changed Compartment Sequence: ', end=' ')
printLinkedList(head)  # This should print 10-->15-->34-->41-->56-->72
print()
print('==============Test Case 3=============')
head = createList(np.array([10, 15, 34, 41, 56, 72]))
print('Original Compartment Sequence: ', end=' ')
printLinkedList(head)
head = remove_compartment(head, 6)
print('Changed Compartment Sequence: ', end=' ')
printLinkedList(head)  # This should print 15-->34-->41-->56-->72
print()
