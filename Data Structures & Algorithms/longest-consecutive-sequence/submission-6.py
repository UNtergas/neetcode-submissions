class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        best = 0
        for n in nums:
            if n-1 not in hashset:
                length = 1
                cur = n
                while cur+length in hashset:
                    length +=1
                best = max(best,length)
        return best