class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ret = [1] * size
        prefix = [1] * size
        suffix = [1] * size
        for i in range(1,size):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(size-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(size):
            ret[i]= prefix[i] * suffix[i]
        return ret

"""
   >
1  2  4  6
1  1  2  8
48 24 6  1 



-1 0 1 2 3 
1 -1 0 0 0 
0  6 6 3 1
"""