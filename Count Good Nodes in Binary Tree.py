#optimal solution
def countGoodNodes_better(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0
        is_good = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        left_good = dfs(node.left, max_val)
        right_good = dfs(node.right, max_val)
        return is_good + left_good + right_good

    return dfs(root, float('-inf'))

# Example usage:
print(countGoodNodes_better(root))  # Output: 4



'''
#practice attempt 1
def countGoodNodes_better(root: TreeNode) -> int:
  def dfs(node,max_val):
    if not node:
      return 0
    is_good=1 if node.val>=max_val else 0
    max_val = max(max_val,node.val)
    left_good = dfs(node.left,max_val)
    right_good=dfs(node.right,max_val)

    return is_good + left_good+right_good
   
   return dfs(root,float('-inf'))
'''


#brute force
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countGoodNodes_brute_force(root: TreeNode) -> int:
    def dfs(node, path):
        if not node:
            return 0
        # Check if the current node is a good node
        is_good = 1 if all(node.val >= val for val in path) else 0
        # Add the current node's value to the path
        path.append(node.val)
        # Recursively count good nodes in the left subtree
        left_good = dfs(node.left, path)
        # Recursively count good nodes in the right subtree
        right_good = dfs(node.right, path)
        # Backtrack: Remove the current node's value from the path
        path.pop()
        # Return the total count of good nodes for this subtree
        return is_good + left_good + right_good

    # Start DFS with an empty path
    return dfs(root, [])

# Example usage:
# Construct the tree [3,1,4,3,null,1,5]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
print(countGoodNodes_brute_force(root))  # Output: 4
