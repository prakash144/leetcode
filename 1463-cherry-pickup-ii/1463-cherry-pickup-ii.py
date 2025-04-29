class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Recursion + Memoisation : O(n * m * m * 9), O(n * m^2)
        n = len(grid)
        m = len(grid[0])
        dp = {}


        def dfs(r, c1, c2):
            # If columns go out of bounds
            if c1 < 0 or c1 >= m or c2 < 0 or c2 >= m:
                return float('-inf')
            
             # if at last row
            if r == n - 1:
                if c1 == c2:
                    return grid[r][c1]
                else:
                    return grid[r][c1] + grid[r][c2]
            
            # check memo 
            if (r, c1, c2) in dp:
                return dp[(r, c1, c2)]

            max_cherries = float('-inf')
            # 9 moves: (left, stay, right) for both robots
            max_cherries = float('-inf')
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    new_c1 = c1 + d1
                    new_c2 = c2 + d2
                    curr = grid[r][c1]
                    if c1 != c2:
                        curr += grid[r][c2]
                    else:
                        cherries = grid[r][c1] + grid[r][c2]
                    max_cherries = max(max_cherries, curr + dfs(r + 1, new_c1, new_c2))
            dp[(r, c1, c2)] = max_cherries
            return max_cherries

        return dfs(0, 0, m - 1)