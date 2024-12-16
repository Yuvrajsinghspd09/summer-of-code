class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={}
        count=0
        for index,num in enumerate(nums):
            if num in freq:
                count+=freq[num]
            freq[num]=freq.get(num,0)+1
        return count
