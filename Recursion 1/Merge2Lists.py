"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

#https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLists(self,prev,l1,l2):
        if l1 == None:
            prev.next = l2
            return
        if l2 == None:
            prev.next = l1
            return
            
        if l1.val<l2.val:
            prev.next = l1
            prev = prev.next
            self.mergeLists(prev,l1.next,l2)
        else:
            prev.next = l2
            prev=prev.next
            self.mergeLists(prev,l1,l2.next)
        
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val < list2.val:
            self.mergeLists(list1,list1.next,list2)
            return list1
        
        self.mergeLists(list2,list1,list2.next)
        return list2
        