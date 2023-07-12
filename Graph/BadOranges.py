"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

"""
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

#Solution

class Solution:

    def infect(self,o,v,grid,m,n):
        x = o[0]
        y = o[1]
        if x<m and x>=0 and y<n and y>=0 and grid[x][y]!=None:
            if grid[x][y]>=v:
                grid[x][y] = v
                self.infect([x+1,y],v+1,grid,m,n)
                self.infect([x-1,y],v+1,grid,m,n)
                self.infect([x,y+1],v+1,grid,m,n)
                self.infect([x,y-1],v+1,grid,m,n)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maximum = (m*n)*2
        badOranges = []
        goodOranges ={}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j]=None
                elif grid[i][j] == 2:
                    grid[i][j]=0
                    badOranges.append([i,j])
                else:
                    grid[i][j]=maximum
                    k = str(i)+'x'+str(j)
                    goodOranges[k]=[i,j]
        
        for o in badOranges:
            self.infect(o,0,grid,m,n)
        
        t = 0
        for o in goodOranges.keys():
            orange = goodOranges[o]
            x=orange[0]
            y=orange[1]
            if grid[x][y] == maximum:
                return -1
            else:
                t = max(t,grid[x][y])
        return t