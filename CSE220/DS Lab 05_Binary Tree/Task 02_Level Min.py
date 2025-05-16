from functions import tree_construction, inorder
def smallest_level(root, level={}, i=0):
    if root == None:
        return
    if i in level.keys():
        if level[i] > root.elem:
            level[i] = root.elem
    else:
        level[i] = root.elem
    smallest_level(root.left, level, i + 1)
    smallest_level(root.right, level, i + 1)
    return level

#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}