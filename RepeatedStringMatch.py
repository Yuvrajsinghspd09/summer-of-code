'''
The time complexity of this solution is O(n * m), 
where n is the length of a and m is the length of b. 
The space complexity is O(n * m) as well, since we create new strings of length up to n * m.

'''

class Solution:
    def repeated_string_match(self, a: str, b: str) -> int:
        # Case 1: b is a substring of a repeated any number of times
        count = (len(b) + len(a) - 1) // len(a)
        repeated_a = a * count
        if b in repeated_a:
            return count

        # Case 2: b is a substring of a repeated a certain number of times plus an additional a
        repeated_a += a
        if b in repeated_a:
            return count + 1

        return -1