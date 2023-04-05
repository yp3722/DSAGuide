'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def matchTraversal(self,treeNode,listHead):
        if listHead == None:
            return True
        
        if treeNode == None:
            return False
        
        if treeNode.val != listHead.val:
            return False

        return self.matchTraversal(treeNode.left,listHead.next) or self.matchTraversal(treeNode.right,listHead.next)

        


    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        MainQ = deque()

        MainQ.append(root)
        while(len(MainQ)!=0):
            x = MainQ.popleft()
            if x == None:
                continue
            if x.val == head.val:
                if self.matchTraversal(x,head):
                    return True
            MainQ.append(x.left)
            MainQ.append(x.right)
        
        return False