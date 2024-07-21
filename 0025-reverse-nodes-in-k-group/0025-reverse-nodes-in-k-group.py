# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        groupPrev = dummyNode
        
        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next
            prev, curr = kthNode.next, groupPrev.next
            while curr!= groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
            
        return dummyNode.next
            
            
    
    def getKthNode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
            
        return node
        