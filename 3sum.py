
#
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer approach and handle duplicates
        result = []  # Initialize the list to store the triplets

        for i in range(len(nums) - 2):  # Iterate up to the third-to-last element
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first element
                continue
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            while left < right:  # Continue until the pointers meet
                total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet
                if total < 0:
                    left += 1  # Increase the left pointer to increase the sum
                elif total > 0:
                    right -= 1  # Decrease the right pointer to decrease the sum
                else:
                    result.append([nums[i], nums[left], nums[right]])  # Add the valid triplet to the result
                    left += 1
                    right -= 1
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result  # Return the list of triplets


#practice attempt 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=len(nums)-1
            while left<right:
                total = nums[i]+nums[left]+nums[right] 
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

