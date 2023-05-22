#Problem
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

#Constraints
"""
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

#Follow up
"""
Follow up:

A straightforward solution using O(mn) space is probably a bad idea.

A simple improvement uses O(m + n) space, but still not the best solution. --> list of x n y indexes to mark as Zero

Could you devise a constant space solution? yes --> use 1st row and 1st col to note indexes to be marked Zero , but when zero in 1st r or c keep 2 flags
"""

#Solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rsize = len(matrix)
        csize = len(matrix[0])
        
        # r = False
        # c = False 
        origin = matrix[0][0]
        
        for i in range(rsize):
            for j in range(csize):
                if matrix[i][j]==0:
                    if i==0:
                        r=True
                    if j==0:
                        c=True
                    
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        
        for i in range(1,rsize):
            if matrix[i][0]==0:
                for j in range(1,csize):
                    matrix[i][j] = 0
        
        for j in range(1,csize):
            if matrix[0][j] == 0:
                for i in range(1,rsize):
                    matrix[i][j]=0