'''
To solve this problem, we need to consider two possible cases for the maximum subarray sum:

Non-Circular Subarray: The maximum subarray does not wrap around, which can be found using Kadane's algorithm.
Circular Subarray: The maximum subarray wraps around, which can be found by considering the minimum subarray sum and using the total sum of the array.
Detailed Steps and Intuition
Maximum Non-Circular Subarray Sum:

This is the straightforward maximum subarray sum problem, which can be solved using Kadane's algorithm.
Maximum Circular Subarray Sum:

To find the maximum circular subarray sum, we can leverage the total sum of the array.
If we subtract the minimum subarray sum from the total sum, we get the maximum circular subarray sum.
Special Case Handling:

If all elements in the array are negative, the result from the circular subarray logic can be misleading. In this case, we should return the result from the non-circular subarray sum calculation.

'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_sum = float('-inf')
            current_sum = 0
            for num in arr:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        # Step 1: Find the maximum subarray sum using Kadane's algorithm
        max_sum = kadane(nums)

        # Step 2: Find the total sum of the array
        total_sum = sum(nums)

        # Step 3: Find the maximum subarray sum of the inverted array
        inverted_max_sum = kadane([-num for num in nums])

        # Step 4: Handle the case when all elements are negative
        if max_sum < 0:
            return max_sum
        
        # Step 5: Return the maximum of non-circular and circular subarray sums
        return max(max_sum, total_sum + inverted_max_sum)

# Example usage:
solution = Solution()
print(solution.maxSubarraySumCircular([5, -3, 5]))  # Output: 10
print(solution.maxSubarraySumCircular([-3, -2, -1]))  # Output: -1










#To find the minimum sum subarray directly, we can modify Kadane's algorithm.
def find_min_subarray_sum(arr):
    min_sum = float('inf')
    current_sum = 0
    for num in arr:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum
