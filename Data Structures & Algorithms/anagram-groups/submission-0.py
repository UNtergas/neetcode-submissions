class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key=[0]*26
            for c in s:
                key[ord(c) - ord('a')]+=1
            tupkey = tuple(key)
            if tupkey in hashmap:
                hashmap[tupkey].append(s)
            else:
                hashmap[tupkey] = [s]
        return list(hashmap.values())