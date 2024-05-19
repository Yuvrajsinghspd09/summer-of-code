''' for all 3 methods
Time Complexity: The algorithm runs in 
O(n) time because it only requires a single pass through the array.
Space Complexity: The space complexity is 
O(1) since it uses a constant amount of extra space, regardless of the input size.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

#Another method
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
    
   
        xor_arr = arr[0]
        for i in range(1, n):
            xor_arr ^= arr[i]

    # XOR of all numbers from 0 to n (inclusive)
        xor_all = 0
        for i in range(n + 1):
            xor_all ^= i

    # XOR of the above two results will give the missing number
        missing_number = xor_arr ^ xor_all
        return missing_number
    

    #another method

    def find_missing_number(arr):
    n = len(arr)
    
    # Calculate the sum of the first n+1 natural numbers
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the sum of elements in the given array
    actual_sum = sum(arr)
    
    # The difference between the expected sum and the actual sum is the missing number
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usage
arr = [0, 1, 3, 4]
print("The missing number is:", find_missing_number(arr))
