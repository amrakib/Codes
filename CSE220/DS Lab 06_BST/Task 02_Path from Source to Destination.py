from PrettyPrint import PrettyPrintTree
from functions import BTNode
def find_Path(root, key):
    temp = []
    def helper(root, key):
        if root == None:
            return
        if root.elem == key:
            temp.append(root.elem)      
        elif root.elem > key:
            temp.append(root.elem)
            helper(root.left, key)
        elif root.elem < key:
            temp.append(root.elem)
            helper(root.right, key)
        return temp if key in temp else "No Path Found"
    return helper(root, key)

#chatGPT
def find_path(root, key):
    if root is None:
        return "No Path Found"  # Return this if the path doesn't exist

    if root.elem == key:
        return f"[{root.elem}]"  # Return the key formatted as a list string

    # Recursively find the path in the left or right subtree
    if root.elem > key:
        path = find_path(root.left, key)
    else:
        path = find_path(root.right, key)

    # If a valid path is found, prepend the current element
    if path != "No Path Found":
        return f"[{root.elem}," + path[1:]  # Combine the current element with the rest of the path

    return "No Path Found"  # Return this if no valid path is found








# DRIVER CODE
root = BTNode(30)
node10 = BTNode(10)
node40 = BTNode(40)
node3 = BTNode(3)
node15 = BTNode(15)
node35 = BTNode(35)
node55 = BTNode(55)

root.left = node10 
root.right = node40
node10.left = node3
node10.right = node15
node40.left = node35
node40.right = node55

print(find_Path(root, 15))
# This should print [30,10,15]

print(find_Path(root, 50))
# This should print No Path Found

