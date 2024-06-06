def max_subarray_sum(nums):
    # Handle the case when the input list is empty
    if not nums:
        return 0
    
    # Initialize current and global max sums
    current_max = global_max = nums[0]
    
    # Traverse through the array starting from the second element
    for num in nums[1:]:
        # Update current max
        current_max = max(num, current_max + num)
        # Update global max if current max is greater
        global_max = max(global_max, current_max)
    
    return global_max

# Example usage
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(max_subarray_sum([1]))  # Output: 1
print(max_subarray_sum([5, 4, -1, 7, 8]))  # Output: 23
print(max_subarray_sum([-1, -2, -3, -4]))  # Output: -1
