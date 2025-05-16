#LeetCode234

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head) -> bool:
    def reverse(head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    tail = reverse(slow)
    print_linked_list(head)
    print_linked_list(tail)
    while tail:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.next
    return True

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

head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

isPalindrome(head)