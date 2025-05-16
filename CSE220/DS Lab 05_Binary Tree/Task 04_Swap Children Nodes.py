from functions import BTNode, inorder, BTPrinter
def swap_child(root, level, M):
    if root == None:
        return
    if  level < M:
        root.left, root.right = root.right, root.left
    swap_child(root.left, level + 1, M)
    swap_child(root.right, level + 1, M)
    return root



#Driver Code
root=BTNode('A')
nodeB = BTNode("B")
nodeC = BTNode("C")
nodeD = BTNode("D")
nodeE = BTNode("E")
nodeF = BTNode("F")
nodeG = BTNode("G")
nodeH = BTNode("H")
nodeI = BTNode("I")
nodeJ = BTNode("J")

root.left = nodeB
root.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.right = nodeF
nodeD.left = nodeG
nodeD.right = nodeH
nodeE.left = nodeI
nodeF.left = nodeJ


print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()
root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H
