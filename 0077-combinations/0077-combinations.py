class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, comb = [], []
        
        def backtrack(i):
            if len(comb) == k:
                res.append(comb.copy())
                return
            if i > n:
                return 
            
            # decicion to include i
            comb.append(i)
            backtrack(i+1)
            # decicion not to include i
            comb.pop()
            backtrack(i+1)
            
        backtrack(1)
        return res
        