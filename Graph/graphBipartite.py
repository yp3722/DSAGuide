""""
Approach 1 : BFS - fairly straightforward

Approach 2 : DFS - Graph has a loop containing odd number of nodes
"""

from collections import deque


class Solution:

    def checkBiBFS(self,node,visited,graph,color):

        q = deque()
        q.append((node,color))

        while(len(q)!=0):
            x = q.popleft()
            for neighbour in graph[x[0]]:
                if visited[neighbour]==0:
                    visited[neighbour]=-1*x[1]
                    q.append((neighbour,-1*x[1]))
                elif visited[neighbour]==x[1]:
                    return False
        return True

    
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        visited = [ 0 for i in range(n)]  # instead of marking it 1 on visited it will be either -1 or 1 representing 2 colors

        for i in range(n):
            if visited[i]==0:
                visited[i]=-1
                res = self.checkBiBFS(i,visited,graph,-1)
                if res == False:
                    return res
        
        return True