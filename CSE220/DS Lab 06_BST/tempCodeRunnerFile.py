def rightmost(root):
    if root == None:
        return None
    if root.right is None:
        return root.elem
    return rightmost(root.right)