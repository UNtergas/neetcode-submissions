class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count+=1
                    self.dfs(row,col,grid)

        return count

    def dfs(self,x,y,grid):
        grid[x][y]="0"
        for (dx,dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
            cur_x,cur_y=x+dx,y+dy
            if 0<=cur_x<len(grid) and 0<=cur_y<len(grid[0]):
                if grid[cur_x][cur_y] == "1":
                    self.dfs(cur_x,cur_y,grid)

        