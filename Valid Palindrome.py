class Solution:
    def isPalindrome(self, s: str) -> bool:
       if s =="":
        return True
    
       cleaned=''
       for char in s:
        if char.isalnum():
            cleaned+=char.lower()
        
       return cleaned ==cleaned[::-1]


#practice attempt 1 with 2 pointer approach
class Solution:
    def isPalindrome(self,s):
        left=0
        right=len(s)-1
        while left <right :
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

#practice attempt 2 with 2 pointer approach
class Solution:
    def is_palindrome(self,s):
        if len(s)==0 or len(s)==1:
            return True
        if len(s)>1:
            left=0
            right=len(s)-1
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        return False
            
    return False

abcba
        
            
