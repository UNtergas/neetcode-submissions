class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        lo,hi = 0, N-1
        target=N - k
        while lo<=hi:
            p=lo
            for i in range(lo,hi+1):
                if nums[i] < nums[hi]:
                    nums[p],nums[i] = nums[i], nums[p]
                    p+=1


            nums[p], nums[hi] = nums[hi], nums[p]
            if p == target:
                return nums[p]
            elif p>target:
                hi=p-1
            else:
                lo=p+1
