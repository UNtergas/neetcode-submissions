class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        current=0
        hashmap=defaultdict(int)
        best=0
        left=0
        for i in range(len(s)):
            hashmap[s[i]]+=1
            current=max(current, hashmap[s[i]])
            if i-left+1 > k+current:
                hashmap[s[left]]-=1
                left+=1
            best=max(best,i-left+1)
        return best




