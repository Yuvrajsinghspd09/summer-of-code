'''
The basic algorithm and thought process behind this solution:
It checks for the conditions that don't require a swap first, potentially saving unnecessary operations.
It uses mutually exclusive conditions (if-elif-else), which is more appropriate for this scenario.
When a swap is needed, it moves both pointers, which can be more efficient in some cases.
It's more readable and follows a clearer logic:

If the left number is even, move the left pointer.
Else if the right number is odd, move the right pointer.
Otherwise (left is odd and right is even), swap and move both pointers.

'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums




#not so efficient because of extra space used
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        even_index = 0
        odd_index = n-1
        for num in nums:
            if num%2==0:
                result[even_index]= num
                even_index+=1
            else:
                result[odd_index]=num
                odd_index-=1
        return result
