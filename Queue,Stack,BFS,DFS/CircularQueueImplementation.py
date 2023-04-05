class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for i in range(k)]
        self.head = -1
        self.tail = -1
        self.ln = k
 
    def enQueue(self, value: int) -> bool:
        if self.isFull() :
            return False
        if self.tail == -1:
            self.head = 0
            self.tail = 0
        elif self.tail == self.ln-1:
            self.tail = 0
        else:
            self.tail+=1
            
        self.queue[self.tail]=value
        
        #print('enqueue : ',self.queue,self.head,self.tail,self.ln)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.head == self.ln-1:
            self.head = 0
        else:
            self.head+=1
        
        #print('dequeue : ',self.queue,self.head,self.tail,self.ln)
        return True
        

    def Front(self) -> int:
        if self.head==-1 :
            return -1
        
        #print('front : ',self.queue,self.head,self.tail,self.ln)
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.tail==-1 :
            return -1
        
        #print('rear : ',self.queue,self.head,self.tail,self.ln)
        return self.queue[self.tail]
        
    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        
        #print('empty? : ',self.queue,self.head,self.tail,self.ln)
        return False

    def isFull(self) -> bool:
        if self.tail+1 == self.head:
            #print('FULL : 1')
            return True
        if self.head == 0 and self.tail == self.ln-1:
            #print('FULL : 2')
            return True
        
        #print('full? : ',self.queue,self.head,self.tail,self.ln)
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()