def isAnagram(s, t):
    return sorted(s) == sorted(t)

'''
An anagram is formed by rearranging the letters of a word or phrase.
 To check if two strings are anagrams, we can compare their sorted versions
'''
# practice attempt 1
def anagram_check(word1,word2):
    return sorted(word1)==sorted(word2)
