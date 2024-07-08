'''
Intuition
The key difference between the maximum sum subarray and the maximum product subarray is that the product can become very large or very small very quickly due to the presence of negative numbers and zeros. This means that, unlike the sum, the product of a subarray can flip between positive and negative values based on the elements of the array.

Key Observations
Negative Numbers: Multiplying two negative numbers results in a positive number, which can be beneficial if we encounter another negative number.
Zeros: Encountering a zero will reset the product, as any number multiplied by zero is zero.
Tracking Both Maximum and Minimum Products: At each position, we need to track both the maximum and minimum products because a very large product can become very small (or negative) and vice versa.

Approach Using Modified Kadane’s Algorithm
Initialize Variables:

max_product: Tracks the maximum product subarray found so far.
min_product: Tracks the minimum product subarray that could potentially become the maximum if multiplied by a negative number.
result: The final result, initialized to the first element of the array.

Iterate Through the Array:

For each element in the array, update the max_product and min_product:
If the current element is negative, swapping the max_product and min_product ensures that we are correctly tracking the potential maximum product.
Update max_product to be the maximum of the current element and the product of the current element with the previous max_product.
Update min_product similarly.
Update the result with the maximum of result and max_product.

Edge Cases:

Arrays with one element.
Arrays containing zeros and negative numbers.
'''



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            
            result = max(result, max_product)
        
        return result
