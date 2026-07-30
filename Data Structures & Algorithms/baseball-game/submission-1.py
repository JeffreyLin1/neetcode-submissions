class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r = []
        for i in operations:
            if i == 'C':
                r.pop()
            elif i == 'D':
                r.append(2*r[len(r)-1])
            elif i == '+':
                r.append(r[len(r)-1] + r[len(r)-2])
            else:
                r.append(int(i))
        return sum(r)