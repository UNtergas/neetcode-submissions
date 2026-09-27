class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot=[]
        fresh=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] ==2:
                    rot.append((row,col))
                if grid[row][col]==1:
                    fresh+=1

        tick=0
        while rot and fresh>0:
            current = rot
            print(current,tick,fresh)
            rot = []
            for (x,y) in current:
                for (dx,dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
                    cur_x,cur_y = x+dx, y+dy
                    if 0<=cur_x<len(grid) and 0<=cur_y<len(grid[0]):
                        if grid[cur_x][cur_y] == 1:
                            rot.append((cur_x,cur_y))
                            grid[cur_x][cur_y] = 2
                            fresh-=1
            tick+=1

        return tick if fresh == 0 else -1
        

            
