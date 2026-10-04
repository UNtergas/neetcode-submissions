class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nmap = defaultdict(list)
        cmap = defaultdict(int)

        for dest,src in prerequisites:
            nmap[src].append(dest)
            cmap[dest]+=1

        count=0
        queue = deque()
        for course in range(numCourses):
            if cmap[course] == 0:
                queue.append(course)
        
        while queue:
            current = queue.popleft()
            count+=1
            for n in nmap[current]:
                cmap[n]-=1
                if cmap[n] == 0:
                    queue.append(n)
        return count==numCourses
                

        