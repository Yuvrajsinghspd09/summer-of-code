def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage


nums3 = [1, 3, 5, 6]
target3 = 7
print(search_insert_position(nums3, target3))  # Output: 4
