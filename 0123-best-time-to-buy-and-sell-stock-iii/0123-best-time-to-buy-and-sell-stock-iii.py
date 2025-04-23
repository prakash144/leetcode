class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

         # DP table: dp[i][j] - max profit with i transactions on day j
        dp = [[0] * n for _ in range(3)]
        
        for i in range(1, 3):
            maxDiff = -prices[0]  # Max difference of previous profit and buying price
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])

        return dp[2][n - 1]
