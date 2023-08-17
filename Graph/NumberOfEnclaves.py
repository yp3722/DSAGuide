class Solution:

    def makeZeroBFS(self,i,j,grid):
        grid[i][j]=0
        q = collections.deque()
        q.append((i,j))
        m = len(grid)
        n = len(grid[0])
        while(len(q)!=0):
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                x = curr[0]
                y = curr[1]

                if x+1<m and grid[x+1][y]==1:
                    grid[x+1][y]=0
                    q.append((x+1,y))
                
                if x-1>=0 and grid[x-1][y]==1:
                    grid[x-1][y]=0
                    q.append((x-1,y))

                if y+1<n and grid[x][y+1]==1:
                    grid[x][y+1]=0
                    q.append((x,y+1))

                if y-1>=0 and grid[x][y-1]==1:
                    grid[x][y-1]=0
                    q.append((x,y-1))       

    def numEnclaves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if grid[i][0]==1:
                self.makeZeroBFS(i,0,grid)
            if grid[i][n-1]==1:
                self.makeZeroBFS(i,n-1,grid)

        for j in range(n):
            if grid[0][j]==1:
                self.makeZeroBFS(0,j,grid)
            if grid[m-1][j]==1:
                self.makeZeroBFS(m-1,j,grid)
               
        return sum([sum(x) for x in grid ])  