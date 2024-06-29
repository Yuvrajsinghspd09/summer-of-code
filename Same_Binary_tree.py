from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are None, trees are equivalent
        if not p and not q:
            return True
        # One of the nodes is None, trees are not equivalent
        if not p or not q:
            return False
        # Values of nodes differ, trees are not equivalent
        if p.val != q.val:
            return False
        # Check the left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

