class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ret = [1] * size
        product=1
        for i in range(1,size):
            product*=nums[i-1]
            ret[i]*=product
        product=1
        for i in range(size-2,-1,-1):
            product*=nums[i+1]
            ret[i]*=product
        return ret

