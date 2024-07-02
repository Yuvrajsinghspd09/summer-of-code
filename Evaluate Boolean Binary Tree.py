'''
not test case
return root.val == 1 effectively does the following:

For a leaf node with value 1, it returns True
For a leaf node with value 0, it returns False
It's a concise way to say: "If the leaf node's value is 1, return True; otherwise (i.e., if it's 0), return False."
'''

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
