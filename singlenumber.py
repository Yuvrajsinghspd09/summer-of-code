'''
Time Complexity: 
O(n) where n is the number of elements in the array. The array is traversed once.
Space Complexity: 
O(1). Only a constant amount of extra space is used.
'''
#Another method below this solution
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # Using XOR operation
    return result

# Example 1
nums1 = [2, 2, 1]
print(singleNumber(nums1))  # Output: 1

# Example 2
nums2 = [4, 1,4,3, 2, 1, 2]
print(singleNumber(nums2))  # Output: 4

# Example 3
nums3 = [1]
print(singleNumber(nums3))  # Output: 1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize an empty dictionary to store frequencies
        freq_dict = {}
        
        # Populate the dictionary with frequencies
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        # Find the single number with frequency 1
        for num, freq in freq_dict.items():
            if freq == 1:
                return num
'''
Time Complexity: 

O(n), where 𝑛
n is the number of elements in the array. We traverse the array once to populate the dictionary and once more to find the single number.
Space Complexity: 
O(n) in the worst case if all elements are distinct and stored in the dictionary.
'''

'''
def singlenumber(nums):
    freq_dict={}
    count=0
    for num in nums:
        if num in dict:
            freq_dict[num]+=1
        else:
            freq_dict[num]=1
        
    for num,freq in freq_dict.items():
        if freq==1:
            return num
'''
