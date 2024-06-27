###Time complexity: O(rows * cols), Space complexity: O(rows * cols).

from collections import deque

def updateMatrix(mat):
    if not mat:
        return mat
    
    rows, cols = len(mat), len(mat[0])
    output = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    '''
    rows = 3
    cols = 4

    output = [[float('inf')] * cols for _ in range(rows)]
    print(output)
    [[inf, inf, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]]

    
    '''
    queue = deque()
    
    # Initialize queue with cells containing 0 and mark them as visited
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                output[i][j] = 0
                queue.append((i, j))
    
    # Define directions for neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and output[nx][ny] > output[x][y] + 1:
                output[nx][ny] = output[x][y] + 1
                queue.append((nx, ny))
    
    return output
