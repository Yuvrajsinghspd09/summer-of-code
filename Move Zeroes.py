class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_z=0
        for current in range(len(nums)):
            if nums[current]!=0:
                nums[n_z],nums[current]=nums[current],nums[n_z]

                n_z+=1
