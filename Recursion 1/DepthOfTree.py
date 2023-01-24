"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol(self,node,n):
        if node == None:
            return n-1
        return max(self.sol(node.left,n+1),self.sol(node.right,n+1))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.sol(root,1)
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol(self,node,n):
        if node == None:
            return n-1
        return max(self.sol(node.left,n+1),self.sol(node.right,n+1))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.sol(root,1)
    