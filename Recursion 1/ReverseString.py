"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def answer(self,i,max_length,s):
        if i == max_length:
            return 
        
        op = self.answer(i+1,max_length,s)
        op.append(s[i])
        return op
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
        
        
        
        