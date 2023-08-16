"""
eg - 
[1,0],[2,0],[3,1],[3,2]


0 : 
1 : 0
2 : 0
3 : 1,5
5 : 1

op = 0, 1, 2, 5, 3


Mem  req - 

processed - O(N)
current path - O(N)

Approach -
DFS
"""

#DFS Approach
# class Solution:

#     def validatePath(self,courseNum,adjList,processed,op):
#         visited = {}
#         stack = []

#         stack.append(courseNum)
#         visited[courseNum] = True

#         while(len(stack)!=0):

#             x = stack[-1]

#             f = True
#             if adjList.get(x)!=None:
#                 for c in adjList.get(x):
#                     if processed[c]!=1:
#                         if visited.get(c)==True:
#                             return False
#                         else:
#                             visited[c] = True
#                             stack.append(c)
#                             f = False
#                             break
                
#             if f==True:
#                 processed[stack.pop()]=1
#                 op.append(x)
#         return True

#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

#         adjList = {}

#         #bulid adjList
#         for requisite in prerequisites:
#             if requisite[0]==requisite[1]:
#                 return []

#             if adjList.get(requisite[0])==None:
#                 adjList[requisite[0]]=[]

#             adjList[requisite[0]].append(requisite[1])


#         processed = [ 0 for i in range(numCourses)]
#         op = []
        
#         for i in range(numCourses):
#             if processed[i]!=1:
#                 res = self.validatePath(i,adjList,processed,op)
#                 if res==False:
#                     return []
        
#         return op




#BFS Approach aka Topological Sorting

"""
Time = O(V+E)
Space = O(V)
"""
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #count incoming nodes for each vertex
        inCount = [0 for i in range(numCourses)]
        
        #build adjList and inCount
        adjList = { i:[] for i in range(numCourses)}
        for req in prerequisites:
            if adjList.get(req[1])==None:
                adjList[req[1]]=[]

            adjList[req[1]].append(req[0])
            inCount[req[0]]+=1

        #FIFO queue
        q = deque()
        
        for i in range(numCourses):
            if inCount[i]==0:
                q.append(i)
        

        res = []
        while(len(q))!=0:
            vert = q.popleft()
            res.append(vert)
            #update its neighbors and if any have satisfied their respective prereq push them to queue
            for neigh in adjList[vert]:
                inCount[neigh]-=1
                if inCount[neigh]==0:
                    q.append(neigh)
            
            #if loop exists the satisfaction condition can't be met and q will starve
        
        if len(res)==numCourses:
            return res

        return []
            
