''' # by dfs method below this solution
Therefore, the time complexity is 
O(m×n), where 
m is the number of rows and 
n is the number of columns in the image.
Space Complexity:
the space complexity is also 
O(m×n) due to the queue storing all pixels in the worst case.
'''

from collections import deque

def floodFill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]
    
    if start_color == color:
        return image
    
    queue = deque([(sr, sc)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        r, c = queue.popleft()
        image[r][c] = color
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                queue.append((nr, nc))
    
    return image

# Example usage:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, color = 1, 1, 2
print(floodFill(image, sr, sc, color))  # Output: [[2,2,2],[2,2,0],[2,0,1]]

# by dfs

def floodFill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]
    
    if start_color == color:
        return image
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color):
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    dfs(sr, sc)
    return image

# Example usage:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, color = 1, 1, 2
print(floodFill(image, sr, sc, color))  # Output: [[2,2,2],[2,2,0],[2,0,1]]
