'''
Time Complexity: O(n+mlogm), where n is the length of the string and m is the number of unique characters in the string.
Space Complexity:O(n), where n is the length of the string.
'''

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        frequency = Counter(s)
        
        # Step 2: Sort characters by frequency in descending order
        sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Construct the result string
        result = ''.join(char * freq for char, freq in sorted_chars)
        
        return result