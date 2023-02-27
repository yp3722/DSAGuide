"""
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""


class Solution:
    def genTrees(self,s,e):
        if s>e:
            return [None]
        if s == e:
            return [TreeNode(s,None,None)]
        
        op = []
        for i in range(s,e+1):
            LeftPermutations = self.genTrees(s,i-1)
            RightPermutations = self.genTrees(i+1,e)
            
            for pl in LeftPermutations:
                for pr in RightPermutations:
                    op.append(TreeNode(i,pl,pr))
        
        return op

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        return self.genTrees(1,n)