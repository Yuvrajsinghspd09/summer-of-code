class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # i would approach the problem using brute force algorithm, even though 2 pointer looks good enough for this question but i would need to sort the array to use that algorithm and if i do so, the basic condition for solving this problem won't be satisfied, so i would like to stick to brute force approach which is using 2 nested for loops
        count=0
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]<target:
                    count+=1
        return count
