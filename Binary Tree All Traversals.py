#inorder
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    traverse(root)
    return result


#preoder
def preorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result

#postorder
def postorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
    traverse(root)
    return result





'''
# Constructing a sample binary tree:
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

print("Inorder Traversal:", inorder_traversal(tree))
print("Preorder Traversal:", preorder_traversal(tree))
print("Postorder Traversal:", postorder_traversal(tree))

#output
         1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

Inorder Traversal: [4, 2, 5, 1, 6, 3, 7]
Preorder Traversal: [1, 2, 4, 5, 3, 6, 7]
Postorder Traversal: [4, 5, 2, 6, 7, 3, 1]
