class MyCalendar:
    
    def __init__(self):
        self.cal = set()

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(startTime, endTime):
            if i in self.cal:
                return False
        for i in range(startTime, endTime):
            self.cal.add(i)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)