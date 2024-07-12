# optimal approach
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            if k != 0:
                remainder = total % k
            else:
                remainder = total
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
        return False


# better approach - TLE error too
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cumulative_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            cumulative_sum[i] = cumulative_sum[i-1] + nums[i-1]
        
        for i in range(n - 1):
            for j in range(i + 2, n + 1):
                sum_subarray = cumulative_sum[j] - cumulative_sum[i]
                if (k == 0 and sum_subarray == 0) or (k != 0 and sum_subarray % k == 0):
                    return True
        return False



# brute force- time limit exceeded
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range (len(nums)-1):
            for j in range(i+2,len(nums)+1):
                if k==0 :
                    if sum(nums[i:j])==0: 
                        return True
                elif sum(nums[i:j])%k==0:
                    return True
        return False
                    
                
        
