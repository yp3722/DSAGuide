"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListSol(self,node):
        if node.next == None:
            return [node,node]
        
        n = self.reverseListSol(node.next)
        n[0].next  = node
        return [node,n[1]]
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        else:
            n = self.reverseListSol(head)
            n[0].next = None
            head = n[1]
            return head