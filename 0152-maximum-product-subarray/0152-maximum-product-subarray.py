class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        
        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            tempMax = currMax  # store the current max before updating
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tempMax, n * currMin, n)
            res = max(res, currMax)
            
        return res