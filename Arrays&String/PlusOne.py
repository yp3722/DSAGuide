"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        if digits[size-1]<9:
            digits[size-1]+=1
            return digits
        
        digits[size-1]=0
        carry = 1
        
        pos = size-2
        while(carry!=0 and pos>=0):
            val = (digits[pos]+carry)%10
            carry = (digits[pos]+carry)//10
            digits[pos] =  val
            pos-=1
        
        if carry!=0:
            digits.insert(0,carry)
        
        return digits
            
            
        