# time complexity - O(N^3)
# space - O(1)
def beautySum(s: str) -> int:
    n = len(s)
    total_beauty = 0
    
    # Iterate over all starting points of substrings
    for i in range(n):
        freq = [0] * 26  # Frequency array for characters 'a' to 'z'
        
        # Iterate over all ending points of substrings starting from 'i'
        for j in range(i, n):
            char_index = ord(s[j]) - ord('a')
            freq[char_index] += 1
            
            # Calculate min and max frequencies of current substring
            max_freq = max(freq)
            min_freq = float('inf')
            
            for k in range(26):
                if freq[k] > 0:
                    min_freq = min(min_freq, freq[k])
            
            # Sum the beauty of the current substring
            if max_freq > min_freq:
                total_beauty += max_freq - min_freq
    
    return total_beauty

# Test cases
print(beautySum("aabcb"))  # Output: 5
print(beautySum("aabcbaa"))  # Output: 17
