class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l=float('inf')
        r=0
        for t in trips:
            l=min(l,t[1])
            r=max(r,t[2])
        diff=[0] * (r-l+1)
        for t in trips:
            diff[t[1]-l]+=t[0]
            diff[t[2]-l]-=t[0]
        currentPas=0
        for d in diff:
            currentPas+=d
            if currentPas > capacity:
                return False
        return True