#method 1
'''
Time Complexity: O(nlogn+m)
O(nlogn) is the time complexity for sorting the array of strings, where 
n is the number of strings.O(m) is the time complexity for comparing the first and last strings, where 
m is the length of the shortest string between the first and last strings.

Space Complexity: 
O(1)
'''

def longest_common_prefix(strings):
    # Step 1: Check if the array is empty
    if not strings:
        return ""

    # Step 2: Sort the array of strings
    strings.sort()

    # Step 3: Compare the first and last strings
    first_string = strings[0]
    last_string = strings[-1]

    # Step 4: Find the common prefix
    i = 0
    while i < len(first_string) and i < len(last_string) and first_string[i] == last_string[i]:
        i += 1

    return first_string[:i]








#method 2
def longest_common_prefix(strings):
    if not strings:
        return ""

    for i, column_chars in enumerate(zip(*strings)):
        if len(set(column_chars)) > 1:
            break
    else:
        i += 1

    return strings[0][:i]

'''
The zip(*strings) part transposes the list of strings into a list of tuples, where each tuple contains the characters at the corresponding positions in all the strings. For example, if strings = ['apple', 'ape', 'application'], then zip(*strings) would give [('a', 'a', 'a'), ('p', 'p', 'p'), ('p', 'e', 'l'), ('l', '', 'i'), ('e', '', 'c')].
The for loop iterates over the transposed list of tuples (with the index i and the characters in each tuple column_chars).
For each tuple column_chars, it checks if all the characters in that tuple are the same using len(set(column_chars)). If the length of the set is greater than 1, it means there are different characters at that position, so it breaks out of the loop.
If the loop completes without breaking, it increments i by 1.


Finally, it returns the prefix of the first string in strings up to the index i using string slicing strings[0][:i].

'''
# Example usage
input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)  # Output: "fl"




#METHOD 3

#Time Complexity: O(S)
#S is the sum of all characters in all strings.
#In the worst case, we compare every character of the first string with every other string, 
#which takes linear time relative to the input size.

#Space Complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(len(prefix)):
            for strg in strs[1:]:
                # # If the current character doesn't match or the index exceeds the current string length
                if i >= len(strg) or strg[i]!=prefix[i]:
                    return prefix[:i]
        
        # If we complete the loop without finding a mismatch, the entire first string is the prefix
        return prefix
        
