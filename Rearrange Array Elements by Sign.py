# brute force
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
 
        result = []
        for i in range(len(pos)):  # or len(neg), they should be equal
            result.append(pos[i])
            result.append(neg[i])
        return result

# same complexity but only one pass
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_index=0
        neg_index=1
        n = len(nums)
        result = [0]*n

        for i in range(len(nums)):
            if nums[i]>0:
                result[pos_index]=nums[i]
                pos_index+=2
        
            else:
                result[neg_index]=nums[i]
                neg_index+=2
        return result

# worse time complexity but optimal space complexity

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if i%2==0:
                if nums[i]<0:
                    j=i+1

                    while j<n and nums[j]<0:
                        j+=1
                    nums[i],nums[j]=nums[j],nums[i]
            else:
                if nums[i]>0:
                    j=i+1
                    while j<n and nums[j]>0:
                        j+=1
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
