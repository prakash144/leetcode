class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = deque()
        negative = deque()
        
        result = []
        
        for n in nums:
            if n < 0:
                negative.append(n)
            else:
                positive.append(n)
            
        for i in range(len(nums)):
            if i % 2:
                result.append(negative.popleft())
            else:
                result.append(positive.popleft())
                
        
        return result
        