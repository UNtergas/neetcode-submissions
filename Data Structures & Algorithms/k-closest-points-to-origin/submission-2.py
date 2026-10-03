import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclide = lambda x,y: x**2 + y**2
        lo,hi=0, len(points)-1
        while lo<=hi:
            r = random.randint(lo, hi)
            points[r], points[hi] = points[hi], points[r]
            pivot_val = euclide(points[hi][0],points[hi][1])
            pivot = lo
            for i in range(lo,hi):
                cur_d = euclide(points[i][0], points[i][1])
                if cur_d <= pivot_val:
                    points[pivot],points[i] = points[i], points[pivot]
                    pivot+=1
            points[hi],points[pivot]=points[pivot],points[hi]
            if pivot==k-1:
                break;
            elif pivot > k-1:
                hi = pivot-1
            else:
                lo = pivot+1
        return points[:k]
    
