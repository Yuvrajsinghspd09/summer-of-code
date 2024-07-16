#optimal solution
def deleteLeaves(root, target):
    if not root:
        return None
    root.left = deleteLeaves(root.left, target)
    root.right = deleteLeaves(root.right, target)
    if not root.left and not root.right and root.val == target:
        return None
    return root


'''
detailed example

     1
    / \
   2   3
  / \
 2   4

We aim to delete all leaf nodes with the value 2.

Initial Call
We call deleteLeaves(root, 2) where root is the root node of the tree (with value 1).

Step-by-Step Execution
1. Root Node (Value = 1)
The root node is 1.
The function is called recursively on the left child (2).
The function is called recursively on the right child (3).
2. Left Subtree of Root Node (Root Value = 2)
The current node is 2.
The function is called recursively on the left child (2).
The function is called recursively on the right child (4).
3. Left Child of Node 2 (Value = 2)
The current node is 2 (left child of the first 2).
The function is called recursively on the left child (None).
The function is called recursively on the right child (None).
Since both children are None, and the value is 2 (the target), the function returns None (this node is deleted).
4. Right Child of Node 2 (Value = 4)
The current node is 4 (right child of the first 2).
The function is called recursively on the left child (None).
The function is called recursively on the right child (None).
Since both children are None, but the value is not 2, the function returns the node 4.
5. Node 2 (After Processing Children)
After processing its children, the first 2 now has:
Left child: None (because the original left child was deleted).
Right child: Node 4.
Since it has one child and is not a leaf, it is not deleted.
The function returns the node 2.
6. Right Subtree of Root Node (Value = 3)
The current node is 3.
The function is called recursively on the left child (None).
The function is called recursively on the right child (None).
Since both children are None, and the value is not 2, the function returns the node 3.
7. Root Node (After Processing Children)
After processing its children, the root node 1 now has:
Left child: Node 2 (with left child None and right child 4).
Right child: Node 3.
The function returns the root node 1.
'''
