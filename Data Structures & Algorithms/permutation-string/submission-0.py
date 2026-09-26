class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for c in s1:
            count_s1[ord(c)-ord('a')]+=1
        
        right=len(s1)-1
    
        # first inti
        for i in range(right+1):
            count_s2[ord(s2[i]) - ord('a')]+=1
        
        if count_s1==count_s2:
            return True
        
        for i in range(right+1, len(s2)):
            count_s2[ord(s2[i])- ord('a')]+=1
            count_s2[ord(s2[i-right-1])- ord('a')]-=1

            if count_s1==count_s2:
                return True

        return False

# a b 

# right =1 
# l e c a b e e 
# 0 1 
