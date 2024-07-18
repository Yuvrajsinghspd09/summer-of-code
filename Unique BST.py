class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize dp array where dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        
        # Base case: There is exactly 1 way to form a BST with 0 nodes (an empty tree)
        dp[0] = 1
        
        # Fill the dp array for all values from 1 to n
        for i in range(1, n + 1):
            # Calculate dp[i] using the number of unique BSTs that can be formed by the left and right subtrees
            for j in range(1, i + 1):
                dp[i] += dp[j-1] * dp[i-j]
        
        # The result for n nodes is stored in dp[n]
        return dp[n]
