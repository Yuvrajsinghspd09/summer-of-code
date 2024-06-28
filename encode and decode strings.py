# easy approach

'''
Explanation:
Encoding:
Join the list of strings using the delimiter ##.
For the input ["neet", "code", "love", "you"]:
The encoded string becomes "neet##code##love##you".
Decoding:
Split the encoded string using the delimiter ##.
The encoded string "neet##code##love##you":
Splits into ["neet", "code", "love", "you"].
'''
class Solution:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return '##'.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        # Special handling to return an empty list if the encoded string is empty
        if s == '':
            return []
        return s.split('##')



# slightly complex one

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}:{s}"
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter
            j = s.find(':', i)
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded