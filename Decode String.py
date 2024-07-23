'''
We define an inner function decode that takes an index as a parameter.
Inside decode, we iterate through the string starting from the given index:

If we encounter a digit, we build up the number.
If we encounter '[', we recursively call decode for the inner content.
If we encounter ']', we return the current result and the current index.
For any other character (letters), we add it to the result.


We multiply the substring returned from the recursive call by the number we've accumulated.
The main function call starts the recursion from index 0 and returns the first element of the tuple (the decoded string).
'''

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index):
            result = ""
            number = 0
            while index < len(s):
                if s[index].isdigit():
                    number = number * 10 + int(s[index])
                elif s[index] == '[':
                    substring, end_index = decode(index + 1)
                    result += number * substring
                    index = end_index
                    number = 0
                elif s[index] == ']':
                    return result, index
                else:
                    result += s[index]
                index += 1
            return result

        return decode(0)[0]
