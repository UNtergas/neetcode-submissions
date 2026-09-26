class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        prefix_hash={0:1}
        ret=0
        for n in nums:
            prefix_sum+=n
            diff = prefix_sum - k
            ret += prefix_hash.get(diff,0)
            prefix_hash[prefix_sum] = 1 + prefix_hash.get(prefix_sum,0)
        return ret