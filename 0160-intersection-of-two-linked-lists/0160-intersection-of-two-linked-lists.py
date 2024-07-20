# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next  
            return length
        lenA = getLength(headA)
        lenB = getLength(headB)
        
        while lenA > lenB:
            lenA -= 1
            headA = headA.next
            
        while lenB > lenA:
            lenB -= 1
            headB = headB.next
            
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None