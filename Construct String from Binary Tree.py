# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, t: Optional[TreeNode]) -> str:
        if not t:
            return ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return f"{t.val}({left})"
        return f"{t.val}({left})({right})"
