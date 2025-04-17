# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def build(min_val, max_val):
            if self.i >= len(preorder):
                return None
            val = preorder[self.i]
            if val < min_val or val > max_val:
                return None

            self.i += 1
            root = TreeNode(val)
            root.left = build(min_val, val - 1)
            root.right = build(val + 1, max_val)

            return root

        self.i = 0
        return build(float("-inf"), float("inf"))