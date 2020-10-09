# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i = headA
        j = headB
        
        while i!=j:
            if i:
                i = i.next
            else:
                i = headB
            if j:
                j = j.next
            else:
                j = headA
        
        return i