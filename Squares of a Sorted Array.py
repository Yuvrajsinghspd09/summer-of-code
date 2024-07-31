'''
Intuition:
We can optimize this by using a two-pointer approach. Since the input array is already sorted, the largest squares will be at the ends of the array
(either the leftmost or rightmost elements, depending on their absolute values). We can compare these elements and build our result array from right to left.
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left=0
        right=n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                result[i]=nums[left]*nums[left]
                left+=1
            else:
                result[i]= nums[right]*nums[right]
                right-=1
        return result


#practice attempt 1
class Solution:
  def sortedArray(self,nums:List[int])->List[int]:
    n = len(nums)
    result = [0]*n
    left=0
    right = n-1
    for i in range(n-1,-1,-1):
      if abs(nums[left])>abs(nums[right]):
        result[i]=nums[left]*nums[left}
      else:
        result[i]= nums[right]*nums[right]
    return result
        
