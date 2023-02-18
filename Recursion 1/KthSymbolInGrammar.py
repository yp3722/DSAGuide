"""
    0
    01
    0110
    01110001
"""


class Solution:
    def op(self,k):
        
        #base cases
        if k == 0:
            return 0
        elif k == 1:
            return 1
        
        n = k//2
        temp = self.op(n)
        
        if k%2 == 0:
            if temp == 1:
                return 1
            else:
                return 0
            
        else: 
            if temp == 1:
                return 0
            else:
                return 1
        
        
        
        
        
    def kthGrammar(self, n: int, k: int) -> int:
        return self.op(k-1)

# you had to understand that the value at pos i was only affected by value at pos i//2 
# and since they only asked for a value at particular position and not the whole pattern at nth line you dont need to generate the whole string
