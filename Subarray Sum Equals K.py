# optimal solution
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        curr_sum = 0
        total = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in count:
                total += count[curr_sum - k]
            count[curr_sum] += 1
        
        return total






# better approach - time limit exceeded error
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        count = 0
        cumm_sum = [0] * (n + 1)
        
        # Correct cumulative sum calculation
        for i in range(1, n + 1):
            cumm_sum[i] = cumm_sum[i-1] + nums[i-1]
        
        # Subarray sum calculation
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if cumm_sum[j] - cumm_sum[i] == k:
                    count += 1
        
        return count





# brute force - time limit exceeded error 
class Solution:
    def subarraySum(self,nums, k):
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count
