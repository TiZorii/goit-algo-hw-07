class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_min_value_in_avl(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.value

root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right = TreeNode(30)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

min_value = find_min_value_in_avl(root)
print("The smallest value in the AVL tree is:", min_value)