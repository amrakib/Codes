#83. Remove Duplicates from Sorted List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return
    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            temp = curr.next
            curr.next = temp.next
            temp.next = None
        else:
            curr = curr.next
    return head

def print_linked_list(head):
    print()
    current = head
    result = ""
    while current is not None:
        result += f"{current.val} -> "
        current = current.next
    result += "None"
    print(result)
    print()

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print_linked_list(deleteDuplicates(head))
