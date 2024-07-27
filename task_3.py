class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def sum_of_values_in_bst(root):
    if root is None:
        return 0
    return root.value + sum_of_values_in_bst(root.left) + sum_of_values_in_bst(root.right)

root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right = TreeNode(30)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

total_sum = sum_of_values_in_bst(root)
print("The sum of all values in the BST is:", total_sum)