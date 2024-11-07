class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Check by skipping either the left or the right character
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
        return True


#practice attempt 1
 l=0
 r=len(s)-1
while l<r:
    if s[l]==s[r]:
        l+=1
        r-=1
    else:
        return s[l+1:r+1]==s[l+1:r+1] or s[l:r]==s[l:r]
return True
