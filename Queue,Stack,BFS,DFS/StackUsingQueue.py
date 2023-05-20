#Problem
"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""

#Follow-up: Can you implement the stack using only one queue?

#Constraints
"""
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
"""

#Solution using one queue
class MyStack:

    def __init__(self):
        self.q = collections.deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size+=1
            
    def pop(self) -> int:
        n = self.size
        for i in range(n-1):
            self.q.append(self.q.popleft())
        self.size-=1
        return self.q.popleft()
        

    def top(self) -> int:
        n = self.size
        for i in range(n-1):
            self.q.append(self.q.popleft())
        top = self.q.popleft()
        self.q.append(top)
        return top

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()