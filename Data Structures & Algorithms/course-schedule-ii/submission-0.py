class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nmap = defaultdict(list)
        cmap = defaultdict(int)
        for dest,src in prerequisites:
            nmap[src].append(dest)
            cmap[dest]+=1
        
        queue = deque()
        for course in range(numCourses):
            if cmap[course] == 0:
                queue.append(course)
            
        ret = []
        count = 0
        while queue:
            current = queue.popleft()
            ret.append(current)
            count+=1
            for n in nmap[current]:
                cmap[n]-=1
                if cmap[n] == 0:
                    queue.append(n)
    
        if count == numCourses:
            return ret
        else:
            return []
            
        
