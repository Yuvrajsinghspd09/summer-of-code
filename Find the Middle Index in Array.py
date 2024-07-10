class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Update left_sum for the current iteration
            left_sum += nums[i]
            
            # Calculate right_sum as total_sum minus left_sum
            right_sum = total_sum - left_sum
            
            # Check if left_sum equals right_sum plus the current element
            if left_sum - nums[i] == right_sum:
                return i
        
        return -1

