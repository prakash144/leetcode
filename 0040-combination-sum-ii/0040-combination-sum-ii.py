class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        currComb = []
        candidates.sort()
        
        #DFS
        def backtrack(i, total):    
            if total == target:
                result.append(currComb.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            currComb.append(candidates[i])
            backtrack(i+1, total + candidates[i])
            currComb.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, total)
            
        backtrack(0,0)
            
        return result
            
            
            
        