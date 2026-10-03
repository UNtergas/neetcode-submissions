class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                s_i,s_temp = stack.pop()
                ret[s_i]= i-s_i
            stack.append((i,temp))
        return ret
            




