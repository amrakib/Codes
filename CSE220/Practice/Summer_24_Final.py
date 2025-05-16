from PrettyPrint import PrettyPrintTree
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BTNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

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

#Question 2: CO5 [2+8 Points]
def rearrange_token(head, pos):
    temp = head
    index = 1
    while temp.next:
        if index == pos - 1:
            newHead = temp.next
            temp.next = None
            temp = newHead
        index += 1
        temp = temp.next
    temp.next = head
    return newHead
    

head = ListNode("A3", ListNode("A9", ListNode("A4", ListNode("A2", ListNode("A7", ListNode("A8", ListNode("A1")))))))
print_linked_list(head)
print_linked_list(rearrange_token(head, 4))


#Question 3: CO4 [10 Points]
def is_valid(root, key) -> bool:
    def helper(root, level):
        if not root or level > len(key) - 1:
            return False
        if root.val == key[level]:
            if not root.left and not root.right:
                return True
            return helper(root.left, level + 1) or helper(root.right, level + 1)
        return False
    return helper(root, 0)

root = BTNode("C", BTNode("S", BTNode("T"), BTNode("E")), BTNode("R", BTNode("M"), BTNode("P", BTNode("D"))))
#Tree Printer
children = lambda node: [child for child in (node.left, node.right) if child]
value = lambda node: str(node.val)
tree_printer = PrettyPrintTree(children, value)
tree_printer(root)

print(is_valid(root, "CS"))
