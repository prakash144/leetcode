class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = [n for n in nums if n > 0]
        negative = [n for n in nums if n < 0]
        
        result = []
        for p, n in zip(positive, negative):
            result.append(p)
            result.append(n)
        
        return result
        