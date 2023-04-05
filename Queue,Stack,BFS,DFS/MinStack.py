"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.s = []
        self.size = -1
        

    def push(self, val: int) -> None:
        if self.size == -1:
            self.s.append([val,val])
            self.size+=1
            return
        if self.s[self.size][1]<val:
            self.s.append([val,self.s[self.size][1]])
            self.size+=1
            return
        self.s.append([val,val])
        self.size+=1

    def pop(self) -> None:
        self.size-=1
        return self.s.pop()[0]
        

    def top(self) -> int:
        return self.s[self.size][0]
        

    def getMin(self) -> int:
        return self.s[self.size][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()