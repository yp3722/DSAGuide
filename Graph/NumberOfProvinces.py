"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

#Contraints
"""
Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

#Solution
from collections import deque
class Solution:
    def BFS(self,adjMat,n,visited,elem):
        
        q = deque()
        q.append(elem)
        visited[elem]=True
        while(len(q)!=0):
            x = q.popleft()
            for i in range(n):
                if x!=i and adjMat[x][i] == 1 and visited[i]==False:
                    visited[i]=True
                    q.append(i)
        
        return visited

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for i in range(n)]
        count = 0
        for v in range(n):
            if visited[v] == False:
                visited = self.BFS(isConnected,n,visited,v)
                count+=1
        
        return count
        