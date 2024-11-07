class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            # Move l to the next letter
            while l < r and not ('A' <= s[l] <= 'Z' or 'a' <= s[l] <= 'z'):
                l += 1
            # Move r to the previous letter
            while l < r and not ('A' <= s[r] <= 'Z' or 'a' <= s[r] <= 'z'):
                r -= 1

            # Swap the letters
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)
