from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Eating rate upper bounded by max(piles) since h >= piles.length
        l, r = 1, max(piles)

        while l <= r:
            mid_eating_rate = (l + r) // 2
            hours_to_consume = sum(map(lambda x : ceil(x / mid_eating_rate), piles))
            
            print(f"{mid_eating_rate = } , {hours_to_consume = }")
            if hours_to_consume > h:
                l = mid_eating_rate + 1
            if hours_to_consume <= h:
                r = mid_eating_rate - 1
        
        return l
        