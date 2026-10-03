class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        nx,ny=newInterval
        for i in range(len(intervals)):
            x,y= intervals[i]
            if ny < x:
                return res+ [[nx,ny]] + intervals[i:]
            elif nx > y:
                res.append([x,y])
            else:
                nx = min(x,nx)
                ny = max(y,ny)
        return res + [[nx,ny]]