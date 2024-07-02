'''
First, observe the pattern:
Row 1: 0
Row 2: 01
Row 3: 0110
Row 4: 01101001
We can notice that each row is formed by taking the previous row and replacing 0 with 01 and 1 with 10.
A key observation is that each row is actually the previous row, followed by the inverse of the previous row.
Row 1: 0
Row 2: 0 | 1
Row 3: 01 | 10
Row 4: 0110 | 1001
This means that the length of each row is double the length of the previous row.
Now, let's think about how to find the kth symbol in the nth row without generating the entire row:

If k is in the first half of the row, it's the same as the kth symbol in the (n-1)th row.
If k is in the second half of the row, it's the opposite of the (k - 2^(n-1))th symbol in the (n-1)th row.


We can use recursion to solve this problem. The base case is when n = 1, where we return 0.
'''


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case: first row has only one symbol '0'
        if n == 1:
            return 0
        
        # Calculate the length of the current row
        current_row_length = 2**(n-1)
        
        # If k is in the second half of the row
        if k > current_row_length // 2:
            # Invert the result of the corresponding position in the first half
            return 1 - self.kthGrammar(n, k - current_row_length // 2)
        
        # If k is in the first half, it's the same as in the previous row
        return self.kthGrammar(n-1, k)

# Example usage
solution = Solution()
print(solution.kthGrammar(4, 5))  # Should print 1

# mathematical solution 
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') % 2
    
'''
Observation: The nth row has 2^(n-1) elements.
Key Insight: The kth symbol in the nth row is determined by the number of 1s in the binary representation of (k-1).
Pattern:

If the count of 1s in binary(k-1) is even, the symbol is 0.
If the count of 1s in binary(k-1) is odd, the symbol is 1.
Let's verify this for the first 8 positions (n = 4):
k     k-1   binary   count of 1s   result
1     0     0        0 (even)      0
2     1     1        1 (odd)       1
3     2     10       1 (odd)       1
4     3     11       2 (even)      0
5     4     100      1 (odd)       1
6     5     101      2 (even)      0
7     6     110      2 (even)      0
8     7     111      3 (odd)       1

'''