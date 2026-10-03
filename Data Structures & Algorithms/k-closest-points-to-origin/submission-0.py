class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda x,y: x**2 + y**2
        heap=[]
        for x,y in points:
            cur_d =  distance(x,y)
            heapq.heappush(heap, (-cur_d,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [[item[1],item[2]] for item in heap]


            