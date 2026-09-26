class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fin_d=0
        for t in trips:
            fin_d=max(fin_d,t[2])
        arr=[0]*fin_d
        trips.sort(key=lambda x: x[1])
        print(trips)
        for t in trips:
            for i in range(t[1],t[2]):
                arr[i]+=t[0]
                if arr[i]>capacity:
                    return False
            
        return True 




