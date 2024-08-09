

# approach 1 using dictionary
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sortrd_str =''.join(sorted(s))
            anagram_map[sortrd_str].append(s)
        return list(anagram_map.values())



# slightly difficult approach but quite gettable

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            # Create a tuple of 26 zeros (one for each letter in the alphabet)
            count = [0] * 26
            
            # Count each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use the tuple of counts as the key
            key = tuple(count)
            anagrams[key].append(s)
        
        return list(anagrams.values())

