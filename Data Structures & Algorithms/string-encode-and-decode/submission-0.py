class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            ret.append(str(len(s))+'#'+s)
        return "".join(ret)
    def decode(self, s: str) -> List[str]:
        ret = []
        index = 0
        
        while index<len(s):
            length = ""
            while s[index]!="#":
                length+=s[index]
                index+=1
            word=""
            index+=1
            for i in range(int(length)):
                word+=s[index]
                index+=1

            ret.append(word)

        return ret
                




