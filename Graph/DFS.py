class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = {}
        stack = [0]
        visited[0]=True
        op = [0]
        while(len(stack)!=0):
            x = stack.pop()
            flag = False
            for v in adj[x]:
                if visited.get(v)==None:
                    stack.append(x)
                    stack.append(v)
                    visited[v]=True
                    op.append(v)
                    break
        return op