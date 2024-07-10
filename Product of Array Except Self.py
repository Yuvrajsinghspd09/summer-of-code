#optimal approach
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Compute the prefix products
        prefix_product = 1
        for i in range(n):
            output[i] *= prefix_product
            prefix_product *= nums[i]
        
        # Compute the suffix products
        suffix_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output



# better approach
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Compute the product of all elements to the left
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        
        # Compute the product of all elements to the right and multiply
        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output



# brute force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Compute the product of all elements to the left
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        
        # Compute the product of all elements to the right and multiply
        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
