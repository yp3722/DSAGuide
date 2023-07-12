#1492. The kth Factor of n
"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""

#Constraints
"""1 <= k <= n <= 1000"""

#Idea
"""
factors of N are distributed as mirror images around the root of N
"""

#Solution
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        greaterThan = []
        root = math.sqrt(n)
        intRoot = int(root)
        f = False 
        if root == intRoot:
            f = True
        c = 0
        for i in range(1, intRoot+1):
            if n%i==0:
                c+=1
                greaterThan.append(n//i)
                if f == True and i == intRoot:
                    greaterThan.pop()
                if c==k:
                    return i

        if len(greaterThan)<k-c:
            return -1
        
        return greaterThan[-1*(k-c)]