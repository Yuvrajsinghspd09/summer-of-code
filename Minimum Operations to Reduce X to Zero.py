# OPTIMAL SOLUTION -O(N)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        left = curr_sum = max_len = 0
        
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len > 0 else -1




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
