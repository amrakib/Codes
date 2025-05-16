from functions import BTNode, BTPrinter


def LCA(root, x, y):
    if root == None:
        return
    if x > root.elem and y > root.elem:
        return LCA(root.right, x, y)
    if x < root.elem and y < root.elem:
        return LCA(root.left, x, y)
    return root.elem


# DRIVER CODE
root = BTNode(15)
node10 = BTNode(10)
node25 = BTNode(25)
node8 = BTNode(8)
node12 = BTNode(12)
node20 = BTNode(20)
node30 = BTNode(30)
node6 = BTNode(6)
node9 = BTNode(9)
node18 = BTNode(18)
node22 = BTNode(22)

root.left = node10
root.right = node25
node10.left = node8
node10.right = node12
node8.left = node6
node8.right = node9
node25.left = node20
node25.right = node30
node20.left = node18
node20.right = node22

print(LCA(root, 6 , 12))
print(LCA(root, 20, 6))
print(LCA(root, 18, 22))
print(LCA(root, 20, 25))
print(LCA(root, 10, 12))
