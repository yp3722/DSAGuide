#2405. Optimal Partition of String

class Solution:
    def partitionString(self, s: str) -> int:
        
        c = 1 
        cet = set()
        for i in range(len(s)):
            if s[i] in cet:
                c+=1
                cet = set()
            cet.add(s[i])  
        return c