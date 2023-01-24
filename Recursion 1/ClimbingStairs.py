"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

class Solution:
    
    def sol(self, n, dic):
        if dic.get(n)!=None:
            return dic[n]
        dic[n] = self.sol(n-1,dic)+self.sol(n-2,dic)
        return dic[n]
    
    def climbStairs(self, n: int) -> int:
        dic = {1:1,2:2}
        return self.sol(n,dic)
        
        
        