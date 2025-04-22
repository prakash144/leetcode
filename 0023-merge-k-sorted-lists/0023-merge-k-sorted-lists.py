# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2    

    def partitionAndMerge(self, start, end, lists):
        if start > end:
            return None

        if start == end:
            return lists[start]

        mid = start + (end - start) // 2
        L1 = self.partitionAndMerge(start, mid, lists)
        L2 = self.partitionAndMerge(mid + 1, end, lists)
        return self.mergeTwoLists(L1, L2)
    
    # START 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None

        return self.partitionAndMerge(0, n - 1, lists)