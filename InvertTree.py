'''
Iterative Approach Using a Queue
Explanation:

Initialize a Queue: Start with the root node in the queue.
Iterate Through the Queue:
Dequeue a node from the front of the queue.
Swap its left and right children.
Enqueue the non-null left and right children.
Continue Until the Queue is Empty: Repeat the process until all nodes have been processed.

'''

# queue method, recursive approach below it
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTreeIterative(root):
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        # Swap the left and right children
        current.left, current.right = current.right, current.left
        
        # Add the children to the queue if they are not None
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return root



'''
Time Complexity: The time complexity of the invertTree method is O(n), where 

n is the number of nodes in the tree. This is because each node is visited once, and for each node,
 constant-time operations (swapping left and right children) are performed.
Space Complexity: The space complexity is also 
O(n) due to the recursion stack. In the worst-case scenario, where the tree is linear (e.g., a linked list), the recursion depth can be 
O(n). However, for balanced trees, the space complexity is typically 
O(logn) due to the depth of the recursion stack
'''

# recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

# Example usage:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted_root = invertTree(root)

def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        print(node.val, end=' ')
        inorderTraversal(node.right)

inorderTraversal(inverted_root)  # Output: 9 7 6 4 3 2 1


















'''


from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
def invertTree(root):
        if not root:
            return None
        

        queue = deque([root])

        while queue:
            
            node= queue.popleft()
            node.left, node.right = node.right, node.left
        
        # Enqueue the left and right children if they exist
            if node.left:
             queue.append(node.left)
            if node.right:
             queue.append(node.right)
    
            return root
        

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted_root = invertTree(root)
'''
