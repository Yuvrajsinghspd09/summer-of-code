class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left= 0
        right = len(numbers)-1
        for i in range (len(numbers)):
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1

#practice attempt 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total==target:
                return left+1,right+1
            elif total>target:
                right-=1
            else:
                left+=1
        return False
