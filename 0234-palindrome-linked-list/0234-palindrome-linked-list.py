# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = self.reversedList(slow)
        fast = head
        
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
    
    def reversedList(self, head):
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
        return prev
        