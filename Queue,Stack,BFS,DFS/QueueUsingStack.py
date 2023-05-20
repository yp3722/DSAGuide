#https://leetcode.com/problems/implement-queue-using-stacks/

#
"""
Follow-up: Can you implement the queue such that each operation
is amortized O(1) time complexity? In other words, performing n 
operations will take overall O(n) time even if one of those 
operations may take longer.

Soln - make push take o(1) time first pop takes n time and consequtive pops will be amortized
"""

from collections import deque
class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()


    def push(self, x: int) -> None:
        s1 = self.s1
        s2 = self.s2
        if len(s1)==0:
            if len(s2)>0:
                while(len(s2)!=0):
                    s1.append(s2.pop())
            s1.append(x)
        elif len(s1)>0 and len(s2)==0:
            s1.append(x)
                
    def pop(self) -> int:
        s1 = self.s1
        s2 = self.s2
        if len(s2)==0:
            if len(s1)>0:
                while(len(s1)!=0):
                    s2.append(s1.pop())
            return s2.pop()
        
        elif len(s2)>0 and len(s1)==0:
            return s2.pop()

    def peek(self) -> int:
        s1 = self.s1
        s2 = self.s2
        if len(s2)!=0:
            x = s2.pop()
            s2.append(x)
            return x
        else:
            x = s1.popleft()
            s1.appendleft(x)
            return x
            
            
            
        

    def empty(self) -> bool:
        s1 = self.s1
        s2 = self.s2
        if max(len(s1),len(s2))==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()