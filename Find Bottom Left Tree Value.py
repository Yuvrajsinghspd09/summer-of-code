#optimal
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([root])
        leftmost = root.val
        
        while queue:
            node = queue.popleft()
            leftmost = node.val
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return leftmost






#brute force
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([(root, 0)])
        leftmost = {0: root.val}
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            
            if depth > max_depth:
                max_depth = depth
                leftmost[depth] = node.val
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return leftmost[max_depth]
