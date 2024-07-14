#optimal
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length


'''
Step-by-step execution:

Initialize:

length = 0
i = len(s) - 1 = 10 (index of the last character)


Skip trailing spaces:

The string "hello world" doesn't have trailing spaces, so this loop is skipped.
i remains 10


Count the characters of the last word:

Start the second while loop
Iteration 1: s[10] = 'd', not a space, so length = 1, i = 9
Iteration 2: s[9] = 'l', not a space, so length = 2, i = 8
Iteration 3: s[8] = 'r', not a space, so length = 3, i = 7
Iteration 4: s[7] = 'o', not a space, so length = 4, i = 6
Iteration 5: s[6] = 'w', not a space, so length = 5, i = 5
Iteration 6: s[5] = ' ', is a space, so the loop ends


Return length, which is 5


'''

# brute force
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string into words
        words = s.split()
        
        # If there are no words, return 0
        if not words:
            return 0
        
        # Return the length of the last word
        return len(words[-1])
