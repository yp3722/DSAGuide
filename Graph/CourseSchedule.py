class Solution:
    def dfs(self,currNode,adj,visited,processed):
        s = [currNode]
        while(len(s)!=0):
            x = s.pop()
            s.append(x)

            f = False
            for node in adj[x]:
                if processed[node]==0:
                    if visited[node]==0:
                        visited[node]=1
                        s.append(node)
                        f = True
                        break
                    else:
                        return False

            if f==False:
                processed[x]=1
                visited[x]=0
                s.pop()

        return True

                 


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a Adjecency List for courses each row denote the ith row  and its columns denote prereq
        adjList = [[] for i in range(numCourses)]
        for item in prerequisites:
            if item[0]!=item[1]:
                adjList[item[0]].append(item[1])
            else:
                return False

        visited = [ 0 for i in range(numCourses)]
        processed = [ 0 for i in range(numCourses)]

        for i in range(numCourses):
            print(i,adjList[i])

        for i in range(numCourses):
            if processed[i]==0 and visited[i]==0:
                visited[i]=1
                res = self.dfs(i,adjList,visited,processed)
                if res == False:
                    return res
        return True


#Approach 2 : Topological Sort - check Course Schedule 2