
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_sum = float('-inf')
            current_sum = 0
            for num in arr:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        total_sum = sum(nums)
        max_sum = kadane(nums)
        
        # Invert the array and find max sum (which is equivalent to finding min sum in original array)
        inverted_max_sum = kadane([-num for num in nums])
        
        # If all numbers are negative, return the max sum (which will be the largest negative number)
        if max_sum < 0:
            return max_sum
        
        # Otherwise, return the maximum of non-circular and circular sum
        return max(max_sum, total_sum + inverted_max_sum)









#To find the minimum sum subarray directly, we can modify Kadane's algorithm.
def find_min_subarray_sum(arr):
    min_sum = float('inf')
    current_sum = 0
    for num in arr:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum
