class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        left = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum > goal: #While the curr_sum is greater than the goal, we remove elements
                                # from the left side of the window by subtracting nums[left] from curr_sum
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == goal:
                count += 1
#in this part we count the subarrays within the current window that have the desired sum goal.
            prev_sum = curr_sum
            for i in range(left, right):
                prev_sum -= nums[i]
                if prev_sum == goal:
                    count += 1
        
        return count