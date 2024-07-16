'''
Thought Process
In-order Traversal: In a BST, an in-order traversal visits nodes in ascending order of their values. This traversal sequence is left subtree -> root -> right subtree.
Counter: Maintain a counter to keep track of the number of nodes visited during the traversal.
Early Exit: Once the counter reaches k, the k-th smallest element has been found, and we can return it immediately, avoiding further unnecessary traversal.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Helper function to perform in-order traversal and find the k-th smallest element
        def in_order(node):
            if not node:
                return None
            
            # Traverse the left subtree
            left_result = in_order(node.left)
            if left_result is not None:
                return left_result  # Return early if k-th smallest is found in left subtree
            
            # Visit the current node
            self.count += 1
            if self.count == k:
                return node.val  # Return if current node is the k-th smallest
            
            # Traverse the right subtree
            right_result = in_order(node.right)
            if right_result is not None:
                return right_result  # Return early if k-th smallest is found in right subtree
            
            return None  # If k-th smallest is not found in this subtree
        
        # Initialize the count to track the number of visited nodes
        self.count = 0
        
        # Start in-order traversal from the root
        return in_order(root)







# brute force
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def in_order_traversal(root: TreeNode) -> list:
    result = []

    def in_order(node):
      if not node:
        return
      in_order(node.left)
      result.append(node.val)
      in_order(node.right)

    in_order(root)
    return result





# practice attempt 1
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Helper function to perform in-order traversal and find the k-th smallest element
        def in_order(node):
          if not node:
            return

            left_result = in_order(root.left)
            if in_order is Not none:
              return result

            self.count+=1
            if self.count==k
              return node.val

            # Traverse the right subtree
            right_result = in_order(node.right)
            if right_result is not None:
                return right_result

            return None

        self.count=0
        return in_order(root)

'''
