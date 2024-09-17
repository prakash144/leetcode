class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        if n == 0: return 0
        if n == 1: return cost[0]
        
        
        # Base cases
        prev2 = 0  # Cost to reach step 0 (ground level)
        prev1 = cost[0]  # Cost to reach step 1
        
        for i in range(2, n+1):
            current = cost[i-1] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
            
            
        return min(prev1, prev2)