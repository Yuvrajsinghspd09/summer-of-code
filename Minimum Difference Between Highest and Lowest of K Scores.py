from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array to ensure contiguous k elements have minimum difference
        result = float('inf')  # Initialize the result with infinity
        left = 0  # Start pointer

        # Iterate from the (k-1)th element to the end of the sorted list
        for right in range(k - 1, len(nums)):
            # Calculate the difference between the highest and lowest scores in the current window
            result = min(result, nums[right] - nums[left])
            left += 1  # Move the left pointer to the right

        return result
