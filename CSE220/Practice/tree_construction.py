from PrettyPrint import PrettyPrintTree
arr = [None, 19, 22, 10, 32, 20, None, 30, None, 5, None, 7, None, None, 2, -2]
class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.left, self.right = None, None

def tree_construction(arr, i=1):
    if i > len(arr) or arr[i] == None:
        return None
    newNode = BTNode(arr[i])
    newNode.left = tree_construction(arr, 2*i)
    newNode.right = tree_construction(arr, 2*i+1)
    return newNode

root = tree_construction(arr)

#Tree Printing
children = lambda node: [child for child in (node.left, node.right) if child]
value = lambda node: str(node.elem)
tree_printer = PrettyPrintTree(children, value)
tree_printer(root)