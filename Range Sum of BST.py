# using dfs
# dfs is more effiecient than bfs and mostly used in such situations

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        total = 0
        
        # If current node's value is in range, add it to total
        if low <= root.val <= high:
            total += root.val
        
        # If current value is greater than low, search left subtree
        if root.val > low:
            total += self.rangeSumBST(root.left, low, high)
        
        # If current value is less than high, search right subtree
        if root.val < high:
            total += self.rangeSumBST(root.right, low, high)
        
        return total
    


# using bfs
from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        total = 0
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if low <= node.val <= high:
                total += node.val
            
            if node.val > low and node.left:
                queue.append(node.left)
            
            if node.val < high and node.right:
                queue.append(node.right)
        
        return total