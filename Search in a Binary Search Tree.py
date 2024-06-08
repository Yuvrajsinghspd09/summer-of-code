'''
def search(root, data):
    if root is None or root.data == data:
        return root
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root, val):
        # Base case: if root is None or root's value matches val, return root
        if root is None or root.val == val:
            return root
        
        # If val is less than root's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If val is greater than root's value, search in the right subtree
        return self.searchBST(root.right, val)
