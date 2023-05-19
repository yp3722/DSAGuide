#Problem
"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""

#Constraints
"""
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

"""

#TestCases
"""
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""

#Soln 
"""
Using stack 
Time Complexity = O(N)
"""

class Solution:
    def processStack(self,s):
        op = ""
        while(len(s)!=0):
            x = s.pop()
            if x != '[':
                op=x+op
            else:
                number = s.pop()
                new_s=""
                for i in range(number):
                    new_s+=op
                s.append(new_s)
                return         
        
    def decodeString(self, s: str) -> str:
        r = len(s)
        stack = []
        i=0
        op=""
        while i < r:
            if s[i]=='[':
                stack.append('[')
                i+=1
                continue
                
            if s[i].isdigit():
                j = i 
                while(j<r):
                    if s[j]=='[':
                        break
                    j+=1
                stack.append(int(s[i:j]))
                i=j
                continue                    
            
            if s[i].isalpha():
                j=i
                while(j<r):
                    if s[j].isalpha():
                        j+=1
                    else:
                        break
                stack.append(s[i:j])
                i=j
                continue
            
            if s[i]==']':
                self.processStack(stack)
                i+=1
                continue
        
        for elem in stack:
            op+=elem
        
        return op