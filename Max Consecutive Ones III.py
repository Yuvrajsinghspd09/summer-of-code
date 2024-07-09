# only the 3rd solution works, first 2 give time limit exceeded error
# Brute Force Approach- Time Complexity: o(n^2) - TIME LIMIT EXCEEDED

'''
Iterate through all possible subarrays.
For each subarray, count the number of 0s.
If the count of 0s is less than or equal to k, update the maximum length if this subarray is longer than the previously found maximum.
'''
def longestOnes(nums, k):
    n = len(nums)
    max_len = 0
    
    for i in range(n):
        zero_count = 0
        for j in range(i, n):
            if nums[j] == 0:
                zero_count += 1
            if zero_count > k:
                break
            max_len = max(max_len, j - i + 1)
    
    return max_len

# Example usage
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))  # Output: 6

#Better Approach (Prefix Sum) - o(n^2)- TIME LIMIT EXCEEDED
'''
Steps:

Construct a prefix sum array to store the number of 0s up to each index.
Iterate through all possible subarrays, and for each subarray, use the prefix sum array to determine the number of 0s.
If the number of 0s is less than or equal to k, update the maximum length.
'''
def longestOnes(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + (1 if nums[i] == 0 else 0)
    
    max_len = 0
    
    for i in range(n):
        for j in range(i, n):
            zero_count = prefix_sum[j + 1] - prefix_sum[i]
            if zero_count <= k:
                max_len = max(max_len, j - i + 1)
    
    return max_len

# Example usage
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))  # Output: 6


#Optimal Approach (Sliding Window)- Time Complexity: O(n)
'''
Steps:

Initialize two pointers left and right.
Expand the window by moving the right pointer and count the number of 0s.
If the count of 0s exceeds k, move the left pointer to the right until the count of 0s is within the limit.
Keep track of the maximum window size.
'''
def longestOnes(nums, k):
    left = 0
    max_len = 0
    zero_count = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Example usage
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))  # Output: 6
