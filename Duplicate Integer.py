

# time complexity- O(n^2)
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    return True
        return False 
    

# time complexity- O(n)

def contains_dup(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
