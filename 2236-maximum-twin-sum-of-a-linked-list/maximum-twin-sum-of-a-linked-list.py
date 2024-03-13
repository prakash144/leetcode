# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hashMap = {}
        i = 0
        res = 0
        cur = head

        while cur:
            hashMap[i] = cur.val
            cur = cur.next
            i += 1

        for i in range(len(hashMap)):
            res = max(res, hashMap[i] + hashMap[len(hashMap)-1-i])

        return res

        


        