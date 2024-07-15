
from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            prev_val = None
            
            for _ in range(size):
                node = queue.popleft()
                
                # Check odd/even condition
                if level % 2 == 0:  # Even-indexed level
                    if node.val % 2 == 0:
                        return False
                    if prev_val is not None and node.val <= prev_val:
                        return False
                else:  # Odd-indexed level
                    if node.val % 2 == 1:
                        return False
                    if prev_val is not None and node.val >= prev_val:
                        return False
                
                prev_val = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True
        
