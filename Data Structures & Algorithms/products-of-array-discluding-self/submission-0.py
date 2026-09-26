class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        c_o = 0
        product = 1
        for n in nums:
            if n == 0:
                c_o+=1
                if c_o > 1:
                    return ret
            else:
                product*=n
 
        for i in range(len(nums)):
            if c_o>0:
                if nums[i] == 0:
                    ret[i] = product
            else:
                ret[i] = product // nums[i]
        return ret
        


# 1  2  4  6
# 1  2  8  48



# 48  24  12  8



# -1  0  1  2  3  0

