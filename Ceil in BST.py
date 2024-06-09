''' 
Expected Time Complexity: O(height of tree)
Expected Space Complexity: O(height of tree)

SOLVED EXAMPLE
       8
      / \
     4   12
    / \   / \
   2   6 10  14
Case 1: Find ceil of 5
Start at 8 (greater than 5, potential ceil).
Move to 4 (less than 5).
Move to 6 (greater than 5, new potential ceil).
Since there’s no further left node, the final ceil is 6.


Case 2: Find ceil of 13
Start at 8 (less than 13).
Move to 12 (less than 13).
Move to 14 (greater than 13, potential ceil).
Since there’s no further left node, the final ceil is 14



'''



class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def findCeil(root, X):
    # Initialize the ceil value as -1 indicating no ceil found
    ceil = -1
    
    while root:
        if root.data == X:
            # If the current node's value is equal to X
            return root.data
        elif root.data > X:
            # If current node's value is greater than X, it could be a potential ceil
            ceil = root.data
            # Move to the left subtree to find a closer value
            root = root.left
        else:
            # Move to the right subtree since the current node's value is less than X
            root = root.right
    
    return ceil
