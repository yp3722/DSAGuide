from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited = {}
        q = Queue()
        q.put(0)
        visited[0]=True
        op = []
        while(q.empty()!=True):
            x = q.get()
            op.append(x)
            for e in adj[x]:
                if visited.get(e)==None:
                    visited[e] = True
                    q.put(e)
        return op