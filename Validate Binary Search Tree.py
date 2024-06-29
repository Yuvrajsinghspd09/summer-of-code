from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # Base case: If the node is None, it's a valid BST by default.
            if not node:
                return True
            # If the current node's value is not in the valid range, return False.
            if not (left < node.val < right):
                return False
            # Recursively check the left and right subtrees with updated boundaries.
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # Initiate the recursion with the root node and the initial boundaries.
        return valid(root, float('-inf'), float('inf'))
