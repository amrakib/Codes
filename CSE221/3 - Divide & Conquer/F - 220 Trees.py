size = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

def post_order(inorder, preorder):
    if not inorder:
        return []
    
    root = preorder.pop(0)
    root_idx = inorder.index(root)

    left = inorder[:root_idx]
    right = inorder[root_idx + 1:]

    return post_order(left, preorder) + post_order(right, preorder) + [root]

postorder = post_order(inorder, preorder)