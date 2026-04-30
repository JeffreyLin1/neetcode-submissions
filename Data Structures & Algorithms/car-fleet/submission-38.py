class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = zip(position, speed)
        cars = sorted([[i, j] for i, j in zipped], key=lambda x: x[0], reverse = True)
        fleets = 0
        stack = []
        for i in cars:
            print(i)
            time = (target-i[0])/i[1]
            print(time)
            if not stack or not time <= stack[-1]:
                stack.append(time)
        return len(stack)



