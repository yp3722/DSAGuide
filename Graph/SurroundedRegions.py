
# DFS SOlution beats 57%
class Solution:
    def dfs(self,x,y,r,c,board,op):
        if x>=0 and x<r and y>=0 and y<c and board[x][y]=='O' and op[x][y]=='X':
            op[x][y]='O'
            self.dfs(x+1,y,r,c,board,op)
            self.dfs(x-1,y,r,c,board,op)
            self.dfs(x,y+1,r,c,board,op)
            self.dfs(x,y-1,r,c,board,op)
        

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        op = [['X' for i in range(c)] for j in range(r)]


        for i in range(r):
            if board[i][0] == 'O':
                #print(i,0)
                self.dfs(i,0,r,c,board,op)
                #print(op)
            
            if board[i][c-1]=='O':
                #print(i,c-1)
                self.dfs(i,c-1,r,c,board,op)
                #print(op)
        
        for j in range(c):
            if board[0][j] == 'O':
                #print(0,j)
                self.dfs(0,j,r,c,board,op)
                # print(op)
            
            if board[r-1][j] == 'O':
                # print(r-1,j)
                self.dfs(r-1,j,r,c,board,op)
                # print(op)
        
        # print("Final")
        # print(op)
        for i in range(r):
            for j in range(c):
                board[i][j] = op[i][j]


# BFS soltion beats 93%, (Mark&Sweep)

class Solution:


    def mark(self,board,i,j,m,n):
        #BFS and Mark all conneced 0s

        q = collections.deque()
        board[i][j]='*'
        q.append((i,j))

        while(len(q)!=0):
            loc = q.popleft()
            x = loc[0]
            y = loc[1]


            if x+1<m and board[x+1][y]=='O':
                board[x+1][y]='*'
                q.append((x+1,y))
            
            if x-1>=0 and board[x-1][y]=='O':
                board[x-1][y]='*'
                q.append((x-1,y))
            
            if y+1<n and board[x][y+1]=='O':
                board[x][y+1]='*'
                q.append((x,y+1))

            if y-1>=0 and board[x][y-1]=='O':
                board[x][y-1]='*'
                q.append((x,y-1))


    def solve(self, board: List[List[str]]) -> None:
        """

        Intuition (BFS) : 
        Check boundary and mark all 0s and their neighbouring 0's as '*' these Zeros are not surrounded by X on all sides
        Finally, make all remaining X as 0 aka captured and make '*' as 0 again

        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                self.mark(board,i,0,m,n)
            if board[i][n-1] == 'O':
                self.mark(board,i,n-1,m,n)
        
        for i in range(n):
            if board[0][i] == 'O':
                self.mark(board,0,i,m,n)
            if board[m-1][i] == 'O':
                self.mark(board,m-1,i,m,n)
        
        #Sweep
        for i in range(m):
            for j in range(n):
                if board[i][j]=='*':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        
        return board

            



