class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            med = (lo+hi)//2
            time = 0
            for bana in piles:
                time+= (bana+med-1) // med
            if h >= time:
                hi=med
            else:
                lo=med+1
        
        return lo
