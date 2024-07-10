# efficient approach - ime Complexity:
#Initialization: O(m*n), where m and n are the dimensions of the matrix.

#sumRegion query: O(1) per query.
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        # Get dimensions of the matrix
        m, n = len(matrix), len(matrix[0])

        # Create a 2D prefix sum matrix with an extra row and column
        # This extra space simplifies our calculations by avoiding edge cases
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the 2D prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the prefix sum for each cell using the formula:
                # current_sum = sum_above + sum_left - sum_overlap + current_value
                self.prefix_sum[i][j] = (
                    self.prefix_sum[i-1][j] +    # Sum of all elements above
                    self.prefix_sum[i][j-1] -    # Sum of all elements to the left
                    self.prefix_sum[i-1][j-1] +  # Remove double-counted overlap
                    matrix[i-1][j-1]             # Add current cell value
                )

        # Theory: At this point, each cell (i,j) in prefix_sum contains
        # the sum of all elements in the submatrix from (0,0) to (i-1,j-1)
        # in the original matrix.

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the sum of the specified region using the formula:
        # region_sum = bottom_right - top_right - bottom_left + top_left
        return (
            self.prefix_sum[row2+1][col2+1] -  # Sum of entire rectangle from (0,0) to (row2,col2)
            self.prefix_sum[row1][col2+1] -    # Subtract rectangle above the target region
            self.prefix_sum[row2+1][col1] +    # Subtract rectangle to the left of the target region
            self.prefix_sum[row1][col1]        # Add back the top-left corner (subtracted twice)
        )

        # Theory: This calculation uses the inclusion-exclusion principle.
        # We start with the sum of the large rectangle, subtract the areas
        # above and to the left of our target region, and then add back
        # the top-left corner which was subtracted twice.







#Better Approach (1D Prefix Sum):
'''Intuition:
We can precompute the row-wise prefix sums to speed up the calculations.
Thought process:

For each row, compute its prefix sum.
For each query, use the row-wise prefix sums to calculate the sum of each row in the specified rectangle, then sum these row sums.
'''

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = self.prefix_sum[i][j-1] + matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            sum += self.prefix_sum[i][col2 + 1] - self.prefix_sum[i][col1]
        return sum



# brute force - time limit exceeded error
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                sum+=self.matrix[i][j]
        return sum
        
