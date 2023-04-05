
#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = []
        operators = ["+", "-", "*","/"]
        op = 0
        for i in range(len(tokens)):
            if tokens[i] in operators:
                a = d.pop()
                b = d.pop()
                if tokens[i]=='+':
                    d.append(a+b)
                elif tokens[i]=='-':
                    d.append(b-a)
                elif tokens[i]=='*':
                    d.append(b*a)
                else:
                    d.append(int(b/a))
            else:
                d.append(int(tokens[i]))        
        return d.pop()