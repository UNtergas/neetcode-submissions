class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')]+=1
            count_s2[ord(s2[i])-ord('a')]+=1

                
        right=len(s1)-1
    
        # first inti
        matching=0
        for i in range(26):
            if count_s1[i] == count_s2[i]:
                matching+=1

        if matching == 26:
            return True
        for i in range(right+1, len(s2)):
            index = ord(s2[i]) - ord('a')
            if count_s1[index] == count_s2[index]:
                matching-=1
            elif count_s1[index] == count_s2[index] + 1:
                matching+=1 
            count_s2[index]+=1
            index = ord(s2[i-right-1])- ord('a')
            if count_s1[index] == count_s2[index]:
                matching-=1
            elif count_s1[index] == count_s2[index]-1:
                matching+=1
            count_s2[index]-=1
            if matching == 26:
                return True
        return False


