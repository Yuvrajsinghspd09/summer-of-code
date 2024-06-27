# solution 1 with time complexity O(n^2)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        for i in range(n):
            left_prod = 1
            right_prod = 1
            
            # Calculate left product
            for j in range(i):
                left_prod *= nums[j]
            
            # Calculate right product
            for k in range(i+1, n):
                right_prod *= nums[k]
            
            # Multiply left and right products
            result[i] = left_prod * right_prod
        
        return result
    

# solution 2 with time complexity O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Arrays to store left and right products
        left_product = [1] * n
        right_product = [1] * n
        
        # Calculate left products
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        
        # Calculate right products
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        
        # Calculate result using left_product and right_product
        output = [left_product[i] * right_product[i] for i in range(n)]
        
        return output
'''
Explanation:
Left Product Calculation: left_product[i] is the product of all elements to the left of nums[i].
Right Product Calculation: right_product[i] is the product of all elements to the right of nums[i].
Result Calculation: output[i] is calculated as left_product[i] * right_product[i], which gives the product of all elements in nums except nums[i].

'''