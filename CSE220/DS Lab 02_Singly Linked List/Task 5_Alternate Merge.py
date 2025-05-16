from __Prerequisite__ import Node, createList, printLinkedList
import numpy as np


def alternate_merge(head1, head2):
    temp1 = head1
    temp2 = head2
    while temp1 != None and temp2 != None:
        lost_1 = temp1.next
        lost_2 = temp2.next
        temp1.next = temp2
        if lost_1 != None:
            temp2.next = lost_1
        temp1 = lost_1
        temp2 = lost_2
    temp1 = head1
    while temp1.next != None:
        temp1 = temp1.next
    temp1.next = Node(None)
    return head1


print('==============Test Case 1=============')
head1 = createList(np.array([1]))
head2 = createList(np.array([5, 7, 3, 9, 4]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
# This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4
printLinkedList(head)


print('==============Test Case 2=============')
head1 = createList(np.array([5, 3, 2, -4]))
head2 = createList(np.array([-4, -6, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)  # This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4


print('==============Test Case 3=============')
head1 = createList(np.array([4, 2, -2, -4]))
head2 = createList(np.array([8, 6, 5, -3]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)  # This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3
