#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def magic(self,node,stack):
        if node.right != None:
                stack.append(node.right)
                node.right = None

        if node.left !=None:
            self.magic(node.left,stack)
        else:
            if len(stack)!=0:
                node.left = stack.pop()
                self.magic(node.left,stack)
    
    def invert(self,node):
        if node!=None:
            if node.left!=None:
                node.right = node.left
                node.left = None
                self.invert(node.right)
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return root
        
        stack = []
        self.magic(root,stack)
        self.invert(root)
        return root