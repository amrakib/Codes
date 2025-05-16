from functions import BTNode, BTPrinter
def subtract_summation(root):
    def sum_node(root):
        if root == None:
            return 0
        return root.elem + sum_node(root.left) + sum_node(root.right)
    return sum_node(root.left) - sum_node(root.right)


# Driver Code
root = BTNode(71)
node27 = BTNode(27)
node62 = BTNode(62)
node80 = BTNode(80)
node75 = BTNode(75)
node41= BTNode(41)
node3 = BTNode(3)
node87 = BTNode(87)
node56 = BTNode(56)
node19 = BTNode(19)
node89 = BTNode(89)

root.left = node27
root.right = node62
node27.left = node80
node27.right = node75
node80.left = node87
node80.right = node56
node62.left = node41
node62.right = node3
node3.left = node19
node3.right = node89

print(subtract_summation(root))  # This should print 111
