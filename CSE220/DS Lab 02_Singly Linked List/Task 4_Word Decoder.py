from __Prerequisite__ import Node, createList, printLinkedList
import numpy as np


def word_Decoder(head):
    temp = head
    count = 0
    while temp != None:
        count += 1
        temp = temp.next
    temp = head
    gap = 13 % count
    new_head = Node(None)
    tail = new_head
    count = count - (count % gap)
    i = 0
    while count > 0:
        if i != count:
            temp = temp.next
            i += 1
        else:
            i = 0
            count -= gap
            tail.next = Node(temp.elem)
            tail = tail.next
            temp = head
    tail.next = None
    return new_head


# Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head)  # This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)  # This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head)  # This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)  # This should print None→N
