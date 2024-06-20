'''
Let's break down the approach step by step:

Start with the root node.
Traverse left until reaching a node with no left child (leftmost leaf).
Return the value of that node as it represents the minimum value in the BST.
 Time Complexity: O(Height of the BST)
 Auxiliary Space: O(1).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minValue(root):
    # If the tree is empty, return -1
    if root is None:
        return -1
    
    # Traverse left until reaching the leftmost leaf node
    while root.left is not None:
        root = root.left
    
    # Return the value of the leftmost leaf node
    return root.val


# practice attempt 1
class TreeNode:
 def __init__(self,val=0,left=None,right=None):
   self.val=val
   self.left=left
   self.right= right

def minValue(root):
  if root is None:
    return -1
   while root.left is not None:
     root= root.left
 return root.val
