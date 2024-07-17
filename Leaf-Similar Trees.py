# brute force
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_nodes(self,root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack,leaves = [root],[]
        while stack:
           node= stack.pop()
           if not node.left and not node.right:
            leaves.append(node.val)
           if node.left:
            stack.append(node.left)
                
           if node.right:
            stack.append(node.right)
                
        return leaves
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaf_nodes(root1)==self.get_leaf_nodes(root2)

        
# another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1) == self.dfs(root2)

