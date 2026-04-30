class MinStack:

    def __init__(self):
        self.s = []
        self.minn = []


    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minn:
            self.minn.append(val)
        else:
            self.minn.append(min(val, self.minn[-1]))


    def pop(self) -> None:
        self.s.pop()
        self.minn.pop()
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minn[-1]
            
        
