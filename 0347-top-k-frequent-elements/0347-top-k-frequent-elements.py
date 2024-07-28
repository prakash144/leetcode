class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0)
            
        freq_items = list(count_map.items())
        freq_items.sort(key=lambda x:x[1], reverse=True)
        
        result = [item[0] for item in freq_items[:k]]
            
        return result 