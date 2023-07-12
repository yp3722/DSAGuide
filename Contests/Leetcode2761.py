#Problem
"""
You are given an integer n. We say that two integers x and y form a prime number pair if:

    1 <= x <= y <= n
    x + y == n
    x and y are prime numbers

Return the 2D sorted list of prime number pairs [xi, yi]. The list should be sorted in increasing order of xi. If there are no prime number pairs at all, return an empty array.

Note: A prime number is a natural number greater than 1 with only two factors, itself and 1.
"""

#Learnings
"""
Eratosthenes Sieve to find primes in range
"""

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        op = []
        if n>3:
            
            prime = [0 for i in range(n+1)]
            prime[0]=1
            prime[1]=1

            for x in range(int(sqrt(n)+1)):
                if prime[x]==0:
                    mulX = x+x
                    while(mulX<(n+1)):
                        prime[mulX]=1
                        mulX+=x
            
            for i in range(1,(n//2)+1):
                if prime[i]==0 and prime[n-i]==0:
                    op.append([i,n-i])
        
        return op
            