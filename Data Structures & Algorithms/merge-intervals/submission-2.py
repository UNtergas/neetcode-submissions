class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = (max(intervals, key=lambda x:x[0]))[0]
        bucket= [-1] * (max_start+1)
        for start,end in intervals:
            bucket[start]=max(bucket[start],end)
        ret =[]
        for i in range(max_start+1):
            if bucket[i] == -1:
                continue
            if ret and ret[-1][1] >= i:
                ret[-1][1] = max(ret[-1][1],bucket[i])
            else:
                ret.append([i,bucket[i]])
        return ret


