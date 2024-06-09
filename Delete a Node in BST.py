'''
Node to be deleted is a leaf (no children):

Simply remove the node from the tree.
Node to be deleted has one child:

Remove the node and replace it with its child.
Node to be deleted has two children:

Find the node's in-order predecessor (the largest node in its left subtree) or its in-order successor (the smallest node in its right subtree).
Replace the node's value with the in-order predecessor or successor's value.
Delete the in-order predecessor or successor node, which will be a leaf node or a node with one child, simplifying the deletion.


'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, key):
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        root.val = minValue(root.right)

        # Delete the inorder successor
        root.right = deleteNode(root.right, root.val)

    return root

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val


'''
Time Complexity:

Average Case: 
O(logn)
Worst Case: 
O(n)

Space Complexity:
Iterative Implementation: 
O(1)
Recursive Implementation:
Average Case: 
O(logn)
Worst Case: 
O(n)


'''