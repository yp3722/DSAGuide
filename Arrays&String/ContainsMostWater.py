#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1

        op = (j-i)*min(height[i],height[j])
        while(i<j):
            opNew = (j-i)*min(height[i],height[j])
            op = max(opNew,op)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return op