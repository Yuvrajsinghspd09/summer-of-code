class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            self.diameter = max(self.diameter, left_height + right_height)
            
            return max(left_height, right_height) + 1
        
        dfs(root)
        return self.diameter
