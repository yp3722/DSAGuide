#Link
# https://leetcode.com/contest/weekly-contest-348/problems/minimize-string-length/

#Solution

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        d = {}
        c=0
        for i in range(len(s)):
            if d.get(s[i])==None:
                d[s[i]]=1
                c+=1
        
        return c


#use set !!