'''
Time Complexity:
The time complexity of this solution is O(k * log n),
 where k is the number of bases to check (n - 2),
 and log n is the time taken to convert the number to a string representation in each base.

 The space complexity of this solution is O(log n), 
 where log n is the maximum length of the string representation of the number in any base.
'''

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_palindrome(s):
            return s == s[::-1]

        for base in range(2, n - 1):
            base_repr = ""
            num = n
            while num > 0:
                base_repr = str(num % base) + base_repr
                num //= base
            if not is_palindrome(base_repr):
                return False

        return True