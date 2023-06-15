"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

"""
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

#Solution
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for x in range(n//2):
            for i in range(x,n-x-1):
                t = matrix[i][n-1-x]
                matrix[i][n-1-x] = matrix[x][i]
                matrix[x][i] = matrix[n-1-i][x]
                matrix[n-1-i][x] = matrix[n-1-x][n-1-i]
                matrix[n-1-x][n-1-i]=t