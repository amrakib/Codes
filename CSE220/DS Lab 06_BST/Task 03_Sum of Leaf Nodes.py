from functions import BTNode
# Task3
def sum_of_leaves(root, sum):
    sum = BTNode(0)

    def add(root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            sum.elem += root.elem
        add(root.left)
        add(root.right)
    add(root)
    return sum.elem


# DRIVER CODE
node30 = BTNode(30)
node10 = BTNode(10)
node40 = BTNode(40)
node3 = BTNode(3)
node15 = BTNode(15)
node35 = BTNode(35)
node55 = BTNode(55)
node2 = BTNode(2)
node36 = BTNode(36)

node30.left = node10
node30.right = node40
node10.left = node3
node10.right = node15
node3.left = node2
node40.left = node35
node40.right = node55
node35.right = node36

print(sum_of_leaves(node30, 0))
