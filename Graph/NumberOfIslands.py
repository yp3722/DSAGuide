from collections import deque
class Solution:

    def isValid(self,x,y,r,c,grid):
        if x<r and y<c and x>-1 and y>-1 and grid[x][y]=="1":
            return True
        return False

    def bfs(self, grid, a, b, m, n):
        q = deque()
        q.append((a,b))

        dirX = [1,-1,0,0]
        dirY = [0,0,1,-1]

        while(len(q)!=0):
            e = q.popleft()
            x = e[0]
            y = e[1]

            for i in range(4):
                if self.isValid(x+dirX[i],y+dirY[i],m,n,grid):
                    grid[x+dirX[i]][y+dirY[i]]="0"
                    q.append((x+dirX[i],y+dirY[i]))
                 
 
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cnt = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    cnt+=1
                    self.bfs(grid,i,j,m,n)
        return cnt