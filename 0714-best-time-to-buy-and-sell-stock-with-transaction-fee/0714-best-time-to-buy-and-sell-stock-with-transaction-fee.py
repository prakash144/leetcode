class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # Greedy Solution - O(n), O(1)
        n = len(prices)
        profit = 0
        buy = prices[0]

        for i in range(1, n):
            # Always look for a cheaper buy
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy + fee: # Sell if profitable (after fee)
                profit += prices[i] - buy - fee
                # update buy to current price to prevent double counting
                buy = prices[i] - fee
        
        return profit
