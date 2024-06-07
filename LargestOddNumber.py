'''
in range(len(num) - 1, -1, -1):

len(num) - 1 is the start value, which is the index of the second-to-last element in the sequence num.
-1 is the stop value, which means the range will stop before reaching -1 (i.e., it will stop at 0).
-1 is the step value, which means the range will decrement by 1 with each iteration.

'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Traverse the string from right to left
        for i in range(len(num) - 1, -1, -1):
            # Check if the current character is an odd digit
            if num[i] in '13579':
                # Return the substring from start to this position
                return num[:i+1]
        # If no odd digit is found, return an empty string
        return ""

# Example usage
sol = Solution()
print(sol.largestOddNumber("52"))    # Output: "5"
print(sol.largestOddNumber("4206"))  # Output: ""
print(sol.largestOddNumber("35427")) # Output: "35427"
