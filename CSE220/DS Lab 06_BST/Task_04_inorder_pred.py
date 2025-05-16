from functions import BTNode, inorder
from PrettyPrint import PrettyPrintTree


def inorder_predecessor(root, x):

    def inorder(root, x, prev):

        if root is None:
            return prev

        if root.elem < x.elem:
            return inorder(root.right, x, root)

        else:
            if root.elem > prev.elem:
                return inorder(root.left, x, prev)
            else:
                return inorder(root.left, x, root)

    return inorder(root, x, root)


# DRIVER CODE
root = BTNode(20)
n1 = BTNode(8)
n2 = BTNode(22)
n3 = BTNode(4)
n4 = BTNode(12)
n5 = BTNode(10)
n6 = BTNode(14)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n4.left = n5
n4.right = n6

print('Given Tree Inorder Traversal: ', end=' ')
inorder(root)  # Given Tree Inorder Traversal:  4 8 10 12 14 20 22
print()

# Tree Print


def child(node): return [child for child in (node.left, node.right) if child]
def elem(node): return str(node.elem)


treeprint = PrettyPrintTree(child, elem)
treeprint(root)

x = root
# Inorder predecessor of node 20: 14
print(
    f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}')
