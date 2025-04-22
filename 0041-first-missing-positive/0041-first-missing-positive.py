class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # OPTIMAL - O(n), O(1)
        size = len(nums)

        contains_1 = False

        for i in range(size):
            # check id 1 is present in original nums
            if nums[i] == 1:
                contains_1 = True
            if nums[i] <= 0 or nums[i] > size: # [1, n]
                nums[i] = 1

        if not contains_1:
            return 1

        for i in range(size):
            num = abs(nums[i])
            idx = num - 1

            if nums[idx] < 0: continue
            nums[idx] *= -1

        for i in range(size):
            if nums[i] > 0:
                return i + 1

        return size + 1