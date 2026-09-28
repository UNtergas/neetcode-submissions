class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        process = deque([])
        if grid[0][0] ==1 or grid[N-1][N-1] == 1:
            return -1
        DIRS = [(0,1),(1,0),(-1,0),(0,-1), (1,1),(1,-1),(-1,-1),(-1,1)]

        # mark every visited as 1
        grid[0][0]=1
        process.append((1,(0,0)))
        while process:
            distance, (x,y) = process.popleft()
            if (x,y) == (N-1,N-1):
                return distance
            for (dx,dy) in DIRS:
                cur_x,cur_y = x+dx,y+dy
                if 0<=cur_x<N and 0<=cur_y<N and grid[cur_x][cur_y] == 0:
                    grid[cur_x][cur_y] =1 
                    process.append((distance+1,(cur_x,cur_y)))
                
        return -1
