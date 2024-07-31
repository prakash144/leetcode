# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.list = []
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            self.list.append(node.val)
            in_order_traversal(node.right)
    
        in_order_traversal(root)
        left, right = 0, len(self.list) - 1
        while left < right:
            current_sum = self.list[left] + self.list[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return False