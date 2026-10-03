"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda inter: inter.start) 
        best = 0
        heap = []
        for inter in intervals:       
            while heap and inter.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,inter.end)
            best=max(best,len(heap))

        return best

