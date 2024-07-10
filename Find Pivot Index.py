


#  optimal
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Right sum is total_sum minus left_sum minus nums[i]
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        
        return -1


#brute force
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1
