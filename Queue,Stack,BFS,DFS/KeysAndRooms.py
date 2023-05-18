
#Problem - https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/
"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

"""



#Constraints 
"""
n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""


#TestCases
"""
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false


Input: rooms = [[][1]]
Output: false

Input: rooms = [[1][]]
Output: True

Input: rooms = [[1][][]]
Output: False

Input: rooms = [[1,2,3][][][]]
Output: True
"""


#BFS SOLUTION
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        processed = {0:1}
        q = collections.deque()
        q.append(0)
        x = 1
        while(len(q)!=0 and x<n) :
            elem = q.popleft()
            for k in rooms[elem]:
                if processed.get(k)==None:
                    q.append(k)
                    processed[k]=1
                    x+=1
        if x<n:
            return False
        return True

#DFS SOLUTION
class Solution2:
    def dfsSoln(self,elem,rooms,x,n,processed):
        
        if x[0] == n:
            return True
        
        for k in rooms[elem]:
            if processed.get(k)==None:
                processed[k]=1
                x[0]+=1
                op = self.dfsSoln(k,rooms,x,n,processed)
                if op ==True:
                    return True
        return False
        
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        processed = {0:1}
        x = [1]
        return self.dfsSoln(0,rooms,x,n,processed)
                    
