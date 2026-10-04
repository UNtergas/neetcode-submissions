class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        l=[-1] * N
        r=[N] * N
        stack = [0]
        for i in range(1,N):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                l[i]= stack[-1]
            stack.append(i)

        stack=[N-1]
        for i in range(N-2,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                r[i]=stack[-1]
            stack.append(i)

        best =0
        for i in range(N):
            area=(r[i] - l[i] -1)*heights[i]
            best=max(best,area)
        
        return best




