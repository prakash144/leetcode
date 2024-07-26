class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count_map = {}
        
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
                
        for num, count in count_map.items():
            if count == 1:
                return num
            
        