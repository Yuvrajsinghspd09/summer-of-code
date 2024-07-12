#optimal
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_freq = {0: 1}  # Initialize with 0 having frequency 1
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Handle negative remainders
            if remainder < 0:
                remainder += k
            
            # If we've seen this remainder before, it means we can form subarrays
            if remainder in remainder_freq:
                count += remainder_freq[remainder]
            
            # Update the frequency of this remainder
            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
        
        return count




# solution using prefix sum - TLE error
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        prefix_sum = [0]*(n+1)
        for i in range(1,n+1):
            prefix_sum[i]= prefix_sum[i-1]+nums[i-1]

        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray_sum = prefix_sum[j] - prefix_sum[i]
                if subarray_sum % k == 0:
                    count += 1
        
        return count
