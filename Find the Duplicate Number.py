## optimal approach
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point of the two runners
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]            # Move slow pointer one step
            fast = nums[nums[fast]]      # Move fast pointer two steps
            if slow == fast:
                break
        
        # Phase 2: Finding the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]            # Move slow pointer one step
            fast = nums[fast]            # Move fast pointer one step
        
        return slow






# brute force - give time limit exceeded error
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return nums[i]
        
        return -1
