#Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/



class Solution:
    def powOptimized(self,x,n):
        if n==1:
            return x
        
        if n%2 == 0:
            return self.powOptimized(x*x,n//2)
        else:
            return x*self.powOptimized(x*x,(n-1)//2)

    def myPow(self, x: float, n: int) -> float:
        if (n==0) or (x==1.0):
            return 1
        
        if n<0:
            x = 1/x
            n = -1*n
        
        return self.powOptimized(x,n)
