class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum=0
        l=0
        r=len(nums)-1
        while l<r:
            pair_sum= nums[l]+nums[r]
            max_pair_sum= max(pair_sum,max_pair_sum)
            l+=1
            r-=1
        return max_pair_sum
