
from collections import deque

def orangesRotting(grid):
    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Initialize the queue for BFS
    queue = deque()
    
    # Count fresh oranges
    fresh_count = 0
    
    # Initialize the queue with all initially rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1
    
    # Directions for the 4 possible movements (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # If there are no fresh oranges, return 0
    if fresh_count == 0:
        return 0
    
    # Initialize the time counter
    minutes_passed = 0
    
    # Perform BFS
    while queue:
        # Number of rotten oranges to process at this level (minute)
        level_size = len(queue)
        
        for _ in range(level_size):
            r, c = queue.popleft()
            
            # Check all 4 directions
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # If the new cell is within bounds and is a fresh orange
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                    # Rotten the fresh orange
                    grid[new_r][new_c] = 2
                    # Add the newly rotten orange to the queue
                    queue.append((new_r, new_c))
                    # Decrease the count of fresh oranges
                    fresh_count -= 1
        
        # If there were rotten oranges at this level, increment the minutes counter
        if queue:
            minutes_passed += 1
    
    # If there are still fresh oranges left, return -1
    return -1 if fresh_count > 0 else minutes_passed

# Example usage:
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotting(grid))  # Output: 4

