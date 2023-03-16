"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are
perfect squares while 3 and 11 are not.
"""


#BFS gets TLE , try DFS with recursion

import math
from collections import deque
class Solution:
    
    
    def numSquares(self, n: int) -> int:
        q = deque()
        q.append([n,0])
        while(len(q)!=0):
            curr = q.popleft()
            if curr[0]==0:
                return curr[1]
            
            r = math.floor(math.sqrt(curr[0]))
            for i in range(1,r+1):
                q.append([curr[0]-(i**2),curr[1]+1])
        
        return -1