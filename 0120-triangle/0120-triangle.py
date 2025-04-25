class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Tabulation (Bottom-Up DP) : O(n^2),  O(n)
        n = len(triangle)
        dp = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            curr_row = [0] * (i + 1)
            for j in range(i + 1):
                curr_row[j] = triangle[i][j] + min(dp[j], dp[j + 1])
            dp = curr_row

        return dp[0]