class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights) - 1
        best =0 
        while left<right:
            bar_l= heights[left]
            bar_r = heights[right]
            water = (right-left) * min(bar_l, bar_r)
            best = max(best,water)
            if bar_l > bar_r:
                right -=1
            elif bar_l < bar_r:
                left+=1
            else:
                right-=1
                left+=1
        
        return best