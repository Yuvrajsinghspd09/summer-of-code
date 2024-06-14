class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

'''
Time Complexity:
The time complexity of this algorithm is O(n),This is because we iterate through the array once
with the pointer j, comparing each element to the previous unique element.

Space Complexity:
The space complexity is O(1) because the removal of duplicates 
is done in-place without using any additional data structures that grow with the size of the input.

#practice attempt 1
def remve_dup(arr):
    if not arr:
        return 0
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]

    return i+1
'''
