class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        for x,y in intervals[1:]:
            prev_x,prev_y = ret[-1]
            if prev_x<=x<=prev_y:
                ret[-1][1] = max(prev_y, y)
            else:
                ret.append([x,y])
       
        return ret






