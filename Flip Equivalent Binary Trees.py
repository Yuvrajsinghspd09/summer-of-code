'''
The problem can be solved by recursively comparing the nodes of both trees. At each node, you have two choices:

Compare the left subtree of the first tree with the left subtree of the second tree and the right subtree of the first tree with the right subtree of the second tree.
Compare the left subtree of the first tree with the right subtree of the second tree and the right subtree of the first tree with the left subtree of the second tree.
If either of these comparisons holds true at every node, then the trees are flip equivalent.
'''

#optimal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to check if two trees are flip equivalent
        def isFlipEquiv(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return (isFlipEquiv(node1.left, node2.left) and isFlipEquiv(node1.right, node2.right)) or \
                   (isFlipEquiv(node1.left, node2.right) and isFlipEquiv(node1.right, node2.left))
        
        return isFlipEquiv(root1, root2)


# another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to serialize the tree in a way that reflects flip equivalence
        def serialize(node):
            if not node:
                return "#"
            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            # Use min and max to ensure the order is consistent
            return f"{node.val}({min(left_serial, right_serial)},{max(left_serial, right_serial)})"
        
        # Serialize both trees and compare
        return serialize(root1) == serialize(root2)
