'''
Time Complexity: 
O(logn), where n is the maximum value between start and goal. 
This is because the time to compute XOR and the number of bits 
is proportional to the number of bits in the numbers, which is logn.
Space Complexity: 
O(1). We use a constant amount of extra space regardless of the input size.
'''
## XOR both numbers and Count the number of set bits (1s) in the XOR result
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Compute the XOR of start and goal
        xor_result = start ^ goal

        # Using bin(xor_result).count('1') to count 1s in the binary representation of xor_result
        return bin(xor_result).count('1')


'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Convert the integers to binary strings and strip the '0b' prefix
        bin_start = bin(start)[2:]
        bin_goal = bin(goal)[2:]
        
        # Pad the shorter string with leading zeros
        max_len = max(len(bin_start), len(bin_goal))
        bin_start = bin_start.zfill(max_len)
        bin_goal = bin_goal.zfill(max_len)
        
        # Count the number of differing bits
        flips = sum(1 for s, g in zip(bin_start, bin_goal) if s != g)
        
        return flips

#both time and space complexity are O(log n) 

'''


class Solution:
    def minimum_bits(start,goal):
         int_num1 = int(start, 2)
         int_num2 = int(goal, 2)

