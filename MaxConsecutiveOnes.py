'''
Time Complexity: 
O(n), where 
n is the length of the array. We traverse the array once.
Space Complexity: 
O(1). Only a fixed amount of extra space is used for variables regardless of the input size.
'''
class Solution:
    def findMaxConsecutiveOnes(nums):
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count = 0
        
        return max_count
'''
def func(nums):
    start=0
    count=0
    max_count=0
    for i in nums:
        if nums[i]==1:
            count+=1
            if count>max_count:
                max_count=count
        else:
            count=0


    return max_count
        '''