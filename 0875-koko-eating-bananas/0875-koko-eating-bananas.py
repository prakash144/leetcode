class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k):
            hour = 0
            for p in piles:
                hour += math.ceil(p / k)

            return hour <= h

        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2 # per hour koko can eat
            if canEatAll(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l

