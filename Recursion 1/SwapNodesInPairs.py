"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairsSol(self,zero):
        
        if zero == None:
            return None
        first = zero.next
        
        if first==None:
            return None
        
        second = first.next
        if second == None:
            return None
        
        first.next = second.next
        second.next = first
        zero.next = second
            
        self.swapPairsSol(first)
        
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        else:
            first = head
            second = head.next
            
            first.next = second.next
            second.next = first
            head = second   
            self.swapPairsSol(first)
        
        return head
                
            
                
            
            