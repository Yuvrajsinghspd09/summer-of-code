# solution 1
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) - 1):
            if ((nums[i-1] < nums[i] and nums[i] < nums[i+1]) 
            or  (nums[i-1] > nums[i] and nums[i] > nums[i+1])):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums




#2nd solution
'''
Sorting and Alternating Merge
A more efficient approach involves sorting the array and then merging the smallest half with the largest half in an alternating manner. 
This ensures that the difference between neighbors is maximized.

Algorithm:

Sort the array.
Split the array into two halves.
Merge the two halves in an alternating manner.
'''
def rearrange_array(nums):
    nums.sort()
    n = len(nums)
    result = []
    
    i, j = 0, (n + 1) // 2
    while i < (n + 1) // 2 and j < n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1
    
    # Append the remaining elements if any
    while i < (n + 1) // 2:
        result.append(nums[i])
        i += 1
    
    while j < n:
        result.append(nums[j])
        j += 1
    
    return result

