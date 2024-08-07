# approach 1 with O(n) time complexity   ,    For O(nlog(n)) scroll down
def kadane_algorithm(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum



Example
Let's take an array nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] and apply Kadane's Algorithm:

Initialize current_sum = -2 and max_sum = -2.
Iterate through nums starting from the second element:
num = 1: current_sum = max(1, -2 + 1) = 1, max_sum = max(-2, 1) = 1
num = -3: current_sum = max(-3, 1 - 3) = -2, max_sum = max(1, -2) = 1
num = 4: current_sum = max(4, -2 + 4) = 4, max_sum = max(1, 4) = 4
num = -1: current_sum = max(-1, 4 - 1) = 3, max_sum = max(4, 3) = 4
num = 2: current_sum = max(2, 3 + 2) = 5, max_sum = max(4, 5) = 5
num = 1: current_sum = max(1, 5 + 1) = 6, max_sum = max(5, 6) = 6
num = -5: current_sum = max(-5, 6 - 5) = 1, max_sum = max(6, 1) = 6
num = 4: current_sum = max(4, 1 + 4) = 5, max_sum = max(6, 5) = 6
The result is max_sum = 6.


When to Use Kadane's Algorithm :

Maximum Subarray Problem: When you need to find the maximum sum of a contiguous subarray in an array of integers.
Efficiently Solving Problems: When you need a linear time solution for finding maximum subarray sum.

Related LeetCode Problems :
Maximum Subarray - LeetCode #53
Maximum Sum Circular Subarray - LeetCode #918
Best Time to Buy and Sell Stock II - LeetCode #122
Maximum Product Subarray - LeetCode #152 (a variation but related in approach)


# approach 2 

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_sum = divide_and_conquer(left, mid)
            right_sum = divide_and_conquer(mid + 1, right)
            cross_sum = find_cross_sum(left, mid, right)
            
            return max(left_sum, right_sum, cross_sum)
        
        def find_cross_sum(left: int, mid: int, right: int) -> int:
            left_max = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_max = max(left_max, current_sum)
            
            right_max = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_max = max(right_max, current_sum)
            
            return left_max + right_max
        
        return divide_and_conquer(0, len(nums) - 1)



