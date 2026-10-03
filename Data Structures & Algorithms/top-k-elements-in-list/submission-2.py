class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n,0)+1
        
        nums_tuple=[(c,n) for (n,c) in hmap.items()]
        heap = nums_tuple[:k]
        heapq.heapify(heap)

        for tup in nums_tuple[k:]:
            if tup > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,tup)
        
        return [v[1] for v in heap]
            