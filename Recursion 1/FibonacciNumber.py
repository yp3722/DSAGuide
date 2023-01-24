# Given n, calculate F(n).

class Solution:
    def sol(self,n,dic):
        if dic.get(n) != None:
            return dic[n]
        else:
            dic[n] = self.sol(n-1,dic) + self.sol(n-2,dic)
            return dic[n]
        
    def fib(self, n: int) -> int:
        dic = {0:0, 1:1}
        return self.sol(n,dic)
        
        
