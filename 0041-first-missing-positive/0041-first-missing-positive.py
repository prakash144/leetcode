class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        size = len(nums) + 1
        seen = [False] * size

        for num in nums:
            if 1 <= num < size:
                seen[num] = True

        for k in range(1, size):
            if not seen[k]:
                return k
        
        return size