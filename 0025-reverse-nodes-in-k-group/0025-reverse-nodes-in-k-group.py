# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        count = 0
        
        # Check if there are at least k nodes left in the list
        while count < k:
            if not node:
                return head
            node = node.next
            count += 1
        
        # Recursively reverse the next k-group
        prev = self.reverseKGroup(node, k)
        
        # Reverse current k-group
        while count > 0:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
            count -= 1
        
        return prev
        