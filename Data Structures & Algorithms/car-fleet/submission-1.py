class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        couple = []
        for i in range(len(position)):
            couple.append((position[i],speed[i]))
        couple.sort(key = lambda x: x[0], reverse=True)

        fleet = []
        for pos,speed in couple:
            time = (target - pos) / speed
            if fleet:
                if time <= fleet[-1]:
                    continue
            
            fleet.append(time)

        return len(fleet)
