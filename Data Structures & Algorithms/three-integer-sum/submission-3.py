class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                current = nums[i] + nums[left] + nums[right]
                if current < 0:
                    left+=1
                elif current > 0:
                    right-=1
                else:
                    ret.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1 
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
        return ret


    
    # n = -4
    
    
    
    # -4 -1 -1  0  1  2 
    #  0  1  2  3  4  5