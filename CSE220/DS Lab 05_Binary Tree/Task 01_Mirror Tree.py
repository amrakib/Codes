from functions import BTNode, inorder, BTPrinter                          # DELETE THIS LINE
temp = BTPrinter()                                                        # DELETE THIS LINE


def convert_mirror(root):
    if root == None:
        return root
    root.right, root.left = root.left, root.right
    convert_mirror(root.left)
    convert_mirror(root.right)
    return root


# DRIVER CODE
root = BTNode(10)
n1 = BTNode(20)
n2 = BTNode(30)
n3 = BTNode(40)
n4 = BTNode(60)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

print('Given Tree Inorder Traversal: ', end=' ')
inorder(root)  # Given Tree Inorder Traversal:  40 20 60 10 30
print()  # DELETE THIS LINE
temp.print_node(root)                                                     # DELETE THIS LINE
root2 = convert_mirror(root)
print('Mirrored Tree Inorder Traversal: ', end=' ')
inorder(root2)  # Mirrored Tree Inorder Traversal:  30 10 60 20 40
print()  # DELETE THIS LINE
temp.print_node(root2)                                                    # DELETE THIS LINE
