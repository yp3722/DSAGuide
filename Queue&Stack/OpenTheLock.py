"""You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""

#https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/

from collections import deque
class Solution:
    
        
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEnds = {}
        mapper = {"0":["9","1"],
                  "1":["0","2"],
                  "2":["1","3"],
                  "3":["2","4"],
                  "4":["3","5"],
                  "5":["4","6"],
                  "6":["5","7"],
                  "7":["6","8"],
                  "8":["7","9"],
                  "9":["8","0"]
                 }
        
        for d in deadends:
            if deadEnds.get(d) == None:
                deadEnds[d]=1
        
        Q = deque()
        
        if deadEnds.get("0000")==None:
            Q.append(['0000',0])
        
        while(len(Q)!=0):
            elem = Q.popleft()
            if elem[0]==target:
                return elem[1]
            
            deadEnds[elem[0]] = 1
            
            for i in range(4):
                if i == 0:
                    newStr1 = mapper[elem[0][0]][0]+elem[0][1:]
                    newStr2 = mapper[elem[0][0]][1]+elem[0][1:]
                    
                elif i == 3:
                    newStr1 = elem[0][0:3]+mapper[elem[0][3]][0]
                    newStr2 = elem[0][0:3]+mapper[elem[0][3]][1]
                    
                else:
                    newStr1 = elem[0][0:i]+mapper[elem[0][i]][0]+elem[0][i+1:]
                    newStr2 = elem[0][0:i]+mapper[elem[0][i]][1]+elem[0][i+1:]
                                    
                if deadEnds.get(newStr1) == None:
                        Q.append([newStr1,elem[1]+1])
                        deadEnds[newStr1] = 1
                if deadEnds.get(newStr2) == None:
                        Q.append([newStr2,elem[1]+1])
                        deadEnds[newStr2] = 1
                
        return -1
                
                