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



# Question 2: CO3 [10 Points]
def hash(head, st) -> int:
    key = 0
    temp = head
    i = 0
    index = -1
    while temp:
        while i < len(st):
            if st[i] == temp.val:
                index = i
            i += 1
        i = 0
        key += index
        index = -1
        temp = temp.next
    return key % 10 

head = ListNode("D", ListNode("A", ListNode("T", ListNode("A"))))
st = "SADA"
print(hash(head, st))

# Question 2: CO3 [10 Points]
def sumTree(root):
    def helper(root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        left = helper(root.left)
        right = helper(root.right)
        return root.val + left + right if left + right == root.val else -1
    return helper(root) == root.val * 2

root = BTNode(26, BTNode(10, BTNode(4), BTNode(6)), BTNode(3, None, BTNode(3)))
#Tree Printer
children = lambda node: [child for child in (node.left, node.right) if child]
value = lambda node: str(node.val)
tree_printer = PrettyPrintTree(children, value)
tree_printer(root)
print(sumTree(root))
