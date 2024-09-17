class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt, max_alt = 0, 0
        
        for g in gain:
            current_alt += g
            max_alt = max(current_alt, max_alt)
            
        return max_alt
        