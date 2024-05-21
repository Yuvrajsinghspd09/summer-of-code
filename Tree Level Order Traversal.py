'''
Time Complexity: The time complexity of this approach is 
O(n), where 𝑛
n is the number of nodes in the tree. Each node is processed once, and for each node, constant-time operations are performed.
Space Complexity: The space complexity is also 
O(n) in the worst case, where all nodes are stored in the queue simultaneously during the traversal.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

root = TreeNode(23)
root.left = TreeNode(39)
root.right = TreeNode(230)
root.right.left = TreeNode(156)
root.right.right = TreeNode(37)

print(levelOrder(root))  
