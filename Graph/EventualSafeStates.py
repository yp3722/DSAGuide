# https://leetcode.com/problems/find-eventual-safe-states/description/


"""
T = O(V+E)
M = O(2V+E)
"""



class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        #Nodes that only go to safe nodes become safe
        """
        So we invert all the links and process the nodes in topological sorted order
        """
        n = len(graph)
        adjNew = { i:[] for i in range(n)}
        inDegree = [0 for i in range(n)]
        for i in range(n):
            for node in graph[i]:
                adjNew[node].append(i)
                inDegree[i]+=1
        
        q = collections.deque()
        for i in range(n):
            if inDegree[i]==0:
                q.append(i)
        op = []
        while(len(q)!=0):

            for i in range(len(q)):
                x = q.popleft()
                op.append(x)
                for neigh in adjNew[x]:
                    inDegree[neigh]-=1
                    if inDegree[neigh]==0:
                        q.append(neigh)
        
        op.sort()
        return op

