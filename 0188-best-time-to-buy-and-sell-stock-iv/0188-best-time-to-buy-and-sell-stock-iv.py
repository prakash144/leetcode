class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0 or k == 0:
            return 0
        
        # If k is larger than n/2, it becomes unlimited transactions problem
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit

        # DP table: dp[i][j] - max profit with i transactions on day j
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            maxDiff = -prices[0]  # Max difference of previous profit and buying price
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]