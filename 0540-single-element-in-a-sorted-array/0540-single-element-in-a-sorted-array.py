from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:  # Change from 'l <= r' to 'l < r' to avoid infinite loop
            m = l + ((r - l) // 2)
            
            if (m % 2 == 1):
                m -= 1  # Ensure m is even so it can be paired with m+1
            
            # If nums[m] == nums[m+1], single element must be on the right side
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        
        return nums[l]
