class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Calculate right sum as total_sum minus left_sum minus nums[i]
            right_sum = total_sum - left_sum - nums[i]
            
            # Compare left_sum and right_sum
            if left_sum == right_sum:
                return i
            
            # Update left_sum for the next iteration
            left_sum += nums[i]
        
        return -1
