'''

Time Complexity:
The time complexity of this approach is O(N), where N is the number of elements in the array. This is because we only iterate through the array once.

Space Complexity:
The space complexity is O(1) as we use only a few variables regardless of the size of the input array.
'''

def longestSubarrayWithSumK(arr, K):
    n = len(arr)
    curr_sum = 0
    max_len = 0
    start = 0
    end = 0
    subarray = []

    while end < n:
        curr_sum += arr[end]
        
        while curr_sum > K:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == K:
            if end - start + 1 > max_len:
                max_len = end - start + 1
                subarray = arr[start:end+1]

        end += 1

    return max_len, subarray


'''
def func(nums,k):
    n=len(nums)
    start=end=0
    current_sum=0
    max_len=0
    subarray=[]

    while end<n:
        current_sum+=end

        if current_sum>k:
            current_sum=current_sum-nums[start]
            start += 1

        if current_sum==k:
            if end - start + 1 > max_len:
                max_len = start-end+1
                subarray=nums[start:end+1]
        
        end+=1

        return max_len,subarray
    

'''