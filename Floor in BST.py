'''
Expected Time Complexity: O(height of tree)
Expected Space Complexity: O(height of tree)
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def floor(root, x):
    # Initialize the floor value as -1 indicating no floor found
    floor_value = -1
    
    while root:
        if root.data == x:
            # If the current node's value is equal to x
            return root.data
        elif root.data < x:
            # If current node's value is less than x, it could be a potential floor
            floor_value = root.data
            # Move to the right subtree to find a closer value
            root = root.right
        else:
            # Move to the left subtree since the current node's value is greater than x
            root = root.left
    
    return floor_value
