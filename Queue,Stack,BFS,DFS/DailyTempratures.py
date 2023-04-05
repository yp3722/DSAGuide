"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        op = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append([temperatures[i],i])
            else:
                while(len(stack)>0 and stack[-1][0]<temperatures[i]):
                    x = stack.pop()
                    op[x[1]] = i-x[1]
                
                stack.append([temperatures[i],i])
        return op