class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node=defaultdict(list)
        for u,v,t in times:
            node[u].append((v,t))

        heap = [(0,k)]
        visited= set() 
        dist = {k:0}
        while heap:
            cur_d, current = heapq.heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            for neighbor, d in node[current]:
                new_d=cur_d+d
                if new_d < dist.get(neighbor,float('inf')):
                    dist[neighbor] = new_d
                    heapq.heappush(heap,(new_d,neighbor))
        if len(visited) < n:
            return -1
        return max(dist.values())