class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            if not s or i > 0 or s[-1] < 0:
                s.append(i)
                continue
            if i == -(s[-1]):
                    s.pop()
                    continue
            while i < -(s[-1]) and s[-1] > 0:
                s.pop()
                if not s or s[-1] < 0:
                    s.append(i)
                    break
                if i == -(s[-1]):
                    s.pop()
                    break
        return s
        


                
