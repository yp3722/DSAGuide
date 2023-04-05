"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


from collections import deque


class Solution:
    def countIsland(self,x,y,m,n,grid):
        
        
        Q = deque([])
        Q.append([x,y])
        
        while(len(Q)!=0):
            pos = Q.popleft()
            i = pos[0]
            j = pos[1]
            
            #terminating conditions
            if i>=0 and j>=0 and i<m and j<n:    
                if grid[i][j]=="1":
                    grid[i][j] = "0"
                    Q.append([i+1,j])
                    Q.append([i-1,j])
                    Q.append([i,j+1])
                    Q.append([i,j-1])
        

    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    self.countIsland(i,j,m,n,grid)
        
        return count
        