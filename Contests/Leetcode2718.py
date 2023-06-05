#Problem
"""
You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.
"""

#Testcase
# https://leetcode.com/contest/weekly-contest-348/problems/sum-of-matrix-after-queries/

#Constraints
"""
Constraints:

1 <= n <= 104
1 <= queries.length <= 5 * 104
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 105
"""

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        N = n*n 
        dqrows ={}
        lendqr = 0
        dqcols = {}
        lendqc = 0
        validQueries = []
        # make queries valid
        for qi in range(len(queries)-1,-1,-1):
            q = queries[qi]
            
            if lendqr+lendqc == N:
                break
            if q[0]==0 and lendqr<n:
                if dqrows.get(q[1])==None:
                    dqrows[q[1]]=True
                    lendqr +=1
                    validQueries.append(q)
            
            elif q[0]==1 and lendqc<n:
                if dqcols.get(q[1])==None:
                    dqcols[q[1]]=True
                    lendqc+=1
                    validQueries.append(q)
        
        #schedule
        r = n
        c = n
        
        op = 0
        for q in validQueries:
            if q[0]==0 and r>0:
                op += (c*q[2])
                r -= 1
            elif c>0:
                op += (r*q[2])
                c -= 1
            
            if c+r == 0:
                break
        
        return op