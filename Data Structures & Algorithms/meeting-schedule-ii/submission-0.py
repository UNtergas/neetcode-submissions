"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hashmap = defaultdict(int)
        for inter in intervals:
            hashmap[inter.start]+=1
            hashmap[inter.end]-=1
        hashmap = tuple(sorted(hashmap.items(),key= lambda x:x[0]))    
        max_room = 0
        prefix = 0
        for _,room in hashmap:
            prefix+=room
            max_room=max(max_room,prefix)
        return max_room