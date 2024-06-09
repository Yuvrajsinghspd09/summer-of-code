#Recursive Approach

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, key):
    # Base case: if the tree is empty, return a new node
    if root is None:
        return Node(key)
    
    # Otherwise, recur down the tree
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    # Return the (unchanged) node pointer
    return root






       
       #ITERATIVE APPROACH


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, key):
    # Create a new node to be inserted
    new_node = Node(key)
    
    # If the tree is empty, the new node becomes the root
    if root is None:
        return new_node

    # Start from the root and find the correct position to insert the new node
    current = root
    parent = None
    
    while current is not None:
        parent = current
        if key < current.data:
            current = current.left
        else:
            current = current.right
    
    # Insert the new node as the left or right child of the parent node
    if key < parent.data:
        parent.left = new_node
    else:
        parent.right = new_node

    return root
