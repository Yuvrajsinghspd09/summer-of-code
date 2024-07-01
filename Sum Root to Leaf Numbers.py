
# by taking initial sum to be 0




# by taking initial sum to be " "
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current_sum: str) -> int:
            if not node:
                return 0
            
            current_sum += str(node.val)
            
            if not node.left and not node.right:
                return int(current_sum)
            
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, "")