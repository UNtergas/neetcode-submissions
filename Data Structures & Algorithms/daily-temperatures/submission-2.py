class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        ret = [0] * N
        for i in range(N-2,-1,-1):
            j=i+1
            while j<N and temperatures[j] <= temperatures[i]:
                if ret[j]==0:
                    j=N
                    break
                j+=ret[j]

            if j<N:
                ret[i]=j-i
        
        return ret
                    