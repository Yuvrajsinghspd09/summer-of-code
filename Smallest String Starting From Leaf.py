#brute force
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        all_paths = []  # Moved this line here

        def dfs(node, path):
            if not node:
                return
            
            # Add current node's value to the path
            path.append(chr(node.val + ord('a')))
            
            if not node.left and not node.right:
                # We've reached a leaf, add the reversed path to our results
                all_paths.append(''.join(reversed(path)))
            else:
                # Continue DFS on children
                dfs(node.left, path)
                dfs(node.right, path)
            
            # Backtrack
            path.pop()

        dfs(root, [])
        
        # Return the lexicographically smallest path
        return min(all_paths) if all_paths else ""


#optimal

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return "~"  # '~' is lexicographically after 'z'
            
            path = chr(node.val + ord('a')) + path
            
            if not node.left and not node.right:
                return path
            
            return min(dfs(node.left, path), dfs(node.right, path))

        return dfs(root, "")
