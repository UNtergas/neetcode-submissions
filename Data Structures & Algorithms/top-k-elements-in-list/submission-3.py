class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for n in nums:
            hmap[n] = hmap.get(n,0)+1
        bucket = [[] for i in range(len(nums))] 
        for n,count in hmap.items():
            bucket[count-1].append(n)
        res=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
    