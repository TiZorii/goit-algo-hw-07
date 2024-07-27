class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_max_value_in_bst(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.value

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

max_value = find_max_value_in_bst(root)
print("The largest value in the BST is:", max_value)