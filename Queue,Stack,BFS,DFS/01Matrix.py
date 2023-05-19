
#Problem 
"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

#Constraints
"""
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

#TestCases
"""
Worst case
1000x1000 matrix with a 0 in last cell
time complexity =(MxN)(MxN)
"""

#Approach 
"""
Process distances in top down and then bottom up and combine results
time complexity = (MxN)
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        op = [[m+n+10 for j in range(n)] for i in range(m)]
        
        #top-down processing
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    op[i][j]=0
                    continue
                
                if i>0:
                    op[i][j]=min(op[i][j],op[i-1][j]+1)
                if j>0:
                    op[i][j]=min(op[i][j],op[i][j-1]+1)
        
        #bottom-up processing
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                
                if i<m-1:
                    op[i][j]=min(op[i][j],op[i+1][j]+1)
                if j<n-1:
                    op[i][j]=min(op[i][j],op[i][j+1]+1)
        
        return op
                