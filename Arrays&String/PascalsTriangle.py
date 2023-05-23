#Problem
"""
Given an integer numRows, return the first numRows of Pascal's triangle.
"""

#Constraints
"""
1 <= numRows <= 30
"""

#Testcases
"""
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

#Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op = [[1]]
        if numRows == 1:
            return op
        else:
            op.append([1,1])
        
        for i in range(2,numRows):
            nextRow = [1]

            for j in range(0,len(op[i-1])-1):
                nextRow.append(op[i-1][j]+op[i-1][j+1])
            nextRow.append(1)
            op.append(nextRow)
        
        return op
        