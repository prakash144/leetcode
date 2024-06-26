class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        start = 0
        
        # Phase 1: Finding the intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Finding the entrance to the cycle
        while slow != start:
            slow = nums[slow]
            start = nums[start]
            
        return slow
        