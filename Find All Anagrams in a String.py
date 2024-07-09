'''

Approach
The optimal approach leverages a sliding window combined with character count arrays (p_count for pattern p and s_count for current window in s) to efficiently determine anagram matches.

Initialization:

Initialize an empty list result to store the starting indices of anagrams.
Check if the length of p is greater than s. If so, return an empty result since p can't fit into s.
Character Count Arrays:

Create two arrays, p_count and s_count, each of size 26 (for the 26 lowercase English letters). These arrays will store the frequency of each character in p and the current window of s, respectively.

Initial Window Setup:

Populate p_count and the first window of s_count with counts of characters from the first len(p) characters of p and s, respectively.
Initial Match Count:

Compare p_count with s_count for each character. Increment a matches counter for each character where the counts match exactly.

Sliding Window:

Slide the window across s from len(p) to len(s).
For each new character added (s[r]) and each character removed (s[l]):
Adjust the respective counts in s_count.
Update matches based on whether the count of the current character matches p_count exactly (matches is incremented or decremented accordingly).
Appending Results:

Whenever matches reaches 26 (indicating all characters match exactly), append the starting index l of the current window to result.

Return Results:

After processing all possible windows, return result containing all starting indices where p is an anagram of the substring in s.
'''


# optimal approach - O(n)
def findAnagrams(s: str, p: str):
    result = []
    if len(p) > len(s):
        return result
    
    # Initialize character count arrays
    p_count = [0] * 26
    s_count = [0] * 26
    
    # Fill p_count with counts of characters in p
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    # Fill s_count with counts of characters in the first window of s
    for i in range(len(p)):
        s_count[ord(s[i]) - ord('a')] += 1
    
    # Check initial match
    matches = 0
    for i in range(26):
        if p_count[i] == s_count[i]:
            matches += 1
    
    # Sliding window approach
    l = 0
    for r in range(len(p), len(s)):
        # Check if current window is an anagram
        if matches == 26:
            result.append(l)
        
        # Slide the window to the right by adding s[r]
        index = ord(s[r]) - ord('a')
        s_count[index] += 1
        if s_count[index] == p_count[index]:
            matches += 1
        elif s_count[index] == p_count[index] + 1:
            matches -= 1
        
        # Slide the window to the left by removing s[l]
        index = ord(s[l]) - ord('a')
        s_count[index] -= 1
        if s_count[index] == p_count[index]:
            matches += 1
        elif s_count[index] == p_count[index] - 1:
            matches -= 1
        
        l += 1
    
    # Check the last window
    if matches == 26:
        result.append(l)
    
    return result


# better approach - O(n*m)

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_p, len_s = len(p), len(s)
        
        if len_p > len_s:
            return result
        
        # Count frequencies of characters in p and the first window in s
        p_count = Counter(p)
        s_count = Counter(s[:len_p])
        
        # Check if the first window is an anagram
        if s_count == p_count:
            result.append(0)
        
        # Start sliding the window
        for i in range(len_p, len_s):
            # Add the new character to the current window count
            s_count[s[i]] += 1
            
            # Remove the character that goes out of the window
            s_count[s[i - len_p]] -= 1
            
            # If the count of the character that went out becomes zero, remove it from the counter
            if s_count[s[i - len_p]] == 0:
                del s_count[s[i - len_p]]
                
            # Compare the current window count with the pattern count
            if s_count == p_count:
                result.append(i - len_p + 1)
        
        return result




# brute force approach - time limit exceeded

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result =[]
        len_p = len(p)
        for i in range(len(s)-len_p+1):
            substring = s[i:i+len_p]
            if sorted(substring) == sorted (p):
                result.append(i)
        return result
