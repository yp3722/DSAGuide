"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        op = ['(','{','[']
        cl = [')','}',']']
        
        d = {')':'(','}':'{',']':'['}
        
        for i in range(len(s)):
            if s[i] in cl:
                if len(stack)==0:
                    return False
                
                if d[s[i]] != stack[-1]:
                    return False
                
                stack.pop()
            
            if s[i] in op:
                stack.append(s[i])
        
        if len(stack)!=0:
            return False
        
        return True
    

# improved memory utilization solution
class Solution:
def isValid(self, s: str) -> bool:
    
    stack = []
    d = {'(':')','{':'}','[':']'}
    
    for i in range(len(s)):
        if s[i] in d.keys():
            stack.append(s[i])
        else:
            if len(stack)==0 or d[stack[-1]]!=s[i]:
                return False
            else:
                stack.pop()
    
    if len(stack)!=0:
        return False
    
    return True
       