'''
Expand Around Center Approach
The idea behind this approach is to consider every possible center of a palindrome and expand around it as long as the characters on both sides are the same. Since a palindrome can be either of odd length (like "aba") or even length (like "abba"), we need to check for both cases.

Here are the detailed steps and explanation:

Consider Each Character as a Center: For each character in the string, consider it as the center of a potential palindrome.
Expand Around the Center: Expand around this center as long as the characters on both sides are the same.
Check Both Odd and Even Lengths: For each center, check for both odd-length palindromes (single character center) and even-length palindromes (pair of characters center).
Keep Track of the Longest Palindrome: Keep track of the longest palindrome found during the expansion process.
Return the Longest Palindrome: After checking all possible centers, return the longest palindrome substring found.


The time complexity of this approach is O(n^2)
The space complexity isO(1)


'''

'''

the line return s[left + 1:right] returns the palindromic substring by 
slicing the original string from the indices just after left and up to (but not including) right.
This works because left and right are pointing
to the indices just outside the palindromic substring after the while loop terminates.
By slicing from left + 1 to right, we get the actual palindromic substring.
'''

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_palindrome = ""

    for i in range(len(s)):
        # Odd-length palindromes
        palindrome = expand_around_center(i, i)
        if len(palindrome) > len(max_palindrome):
            max_palindrome = palindrome

        # Even-length palindromes
        palindrome = expand_around_center(i, i + 1)
        if len(palindrome) > len(max_palindrome):
            max_palindrome = palindrome

    return max_palindrome