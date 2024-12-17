def isAnagram(s, t):
    return sorted(s) == sorted(t)

'''
An anagram is formed by rearranging the letters of a word or phrase.
 To check if two strings are anagrams, we can compare their sorted versions
'''
# optimal approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count= [0]*26
        for i in range(len(s)): # or for i in range(len(t))
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        return all( x==0 for x in count)
