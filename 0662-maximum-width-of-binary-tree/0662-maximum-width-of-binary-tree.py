# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root, 0)])  # Queue stores tuples of (node, index)
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]  # Index of the first node in the current level
            
            for _ in range(level_length):
                node, index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            
            # Calculate width of the current level
            max_width = max(max_width, index - first_index + 1)
        
        return max_width


        