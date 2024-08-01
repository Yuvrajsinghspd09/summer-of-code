class Solution:
    def isPalindrome(self, s: str) -> bool:
       if s =="":
        return True
    
       cleaned=''
       for char in s:
        if char.isalnum():
            cleaned+=char.lower()
        
       return cleaned ==cleaned[::-1]
