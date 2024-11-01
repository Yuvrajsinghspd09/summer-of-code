from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array first
        quadruplets = []
        n = len(nums)
        
        # First two loops to fix the first two elements of the quadruplet
        for i in range(n - 3):
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicate elements for the second position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third and fourth positions
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets


#practice attempt 1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results= set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while l<r:
                   total=nums[l]+nums[r]+nums[i]+nums[j]
                   if total==target:
                    result.add((nums[l],nums[r],nums[i],nums[j]))
                   elif total<target:
                    l+=1
                   else:
                    r-=1
        return [list(quad) for quad in result ]
                
