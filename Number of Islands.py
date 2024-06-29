from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        def dfs(i, j):
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                grid[i][j] == '0' or 
                (i, j) in visited):
                return
            
            visited.add((i, j))  # Mark land cell as visited
            
            # Check all 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        
        return islands
    











#practice attempt 1
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        
        rows,cols=len(grid),len(grid[0])
        islands=0
        visited=set()
        
        def dfs(i,j):
            if (i<0 or i>len(rows) or 
                j<0 or j>len(cols) or
                grid[i,j]=='0' or
                (i,j) in visited):
                return
            
            else:
                visited.add((i,j))
            #check all 4 directions

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        

        for i in range(rows):
            for j in range(cols):
                if grid[i,j]=='1'and (i,j) not in visited:
                    islands+=1
                    dfs(i,j)
        return islands

