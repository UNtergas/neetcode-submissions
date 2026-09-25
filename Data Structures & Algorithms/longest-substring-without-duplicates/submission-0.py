class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = [0] * 128
        left=0
        best=0
        for i in range(len(s)):
            if hashmap[ord(s[i])] > 0:
                left=max(left,hashmap[ord(s[i])])          
            hashmap[ord(s[i])]=i+1
            best=max(best, i-left+1)
        
        return best



#   | 
# z x y z x y z
# 0 1 2 3 4 5 6



# left=1

# z:1
# x;2
# y:3


# i=3 
# 3-1+1 
