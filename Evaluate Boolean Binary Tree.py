class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val == 1
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        
        if root.val == 2:
            return left or right
        else:  # root.val == 3
            return left and right