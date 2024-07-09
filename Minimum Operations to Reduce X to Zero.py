




# brute force - time limit exceeded error
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_ops = float('inf')
        
        for left in range(n + 1):
            for right in range(n + 1):
                if left + right > n:
                    break
                current_sum = sum(nums[:left]) + sum(nums[n-right:])
                if current_sum == x:
                    min_ops = min(min_ops, left + right)
        
        return min_ops if min_ops != float('inf') else -1
