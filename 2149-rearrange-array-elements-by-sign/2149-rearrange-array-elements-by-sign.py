class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = deque()
        negative = deque()
        
        # Separate positive and negative numbers
        for n in nums:
            if n < 0:
                negative.append(n)
            else:
                positive.append(n)
        
        # Alternate between positive and negative for the result
        result = []
        for _ in range(len(nums) // 2):
            result.append(positive.popleft())
            result.append(negative.popleft())
        
        return result
        