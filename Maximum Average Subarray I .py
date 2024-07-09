# with brute force o(n)- time limit exceeds 
# optimal solution at the end
def findMaxAverage(nums, k):
    n = len(nums)
    max_sum = float('-inf')
    for i in range(n - k + 1):
        current_sum = sum(nums[i:i+k])
        max_sum = max(max_sum, current_sum)
    return max_sum / k

# Example usage
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # Output: 12.75


# optimal solution - o(n) complexity too
def findMaxAverage(nums, k):
    n = len(nums)
    max_sum = sum(nums[:k])
    current_sum = max_sum
    for i in range(k, n):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k

# Example usage
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # Output: 12.75
