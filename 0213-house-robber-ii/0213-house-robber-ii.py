class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_helper(nums):
            prev1, prev2 = 0, 0

            #[prev2, prev1, n, n+1, ....]
            for house in nums:
                curr = max(prev2 + house, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))