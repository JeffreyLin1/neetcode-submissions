class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mi = max(weights)
        ma = sum(weights)
        while mi <= ma:
            d = (mi + ma)//2
            res = self.search(weights, days, d)
            if res == 1: 
                mi = d + 1
            elif res == -1: 
                ma = d - 1
        return mi

    def search(self, weights, days, capacity):
        currDays = 1
        currWeight = 0
        for i in weights:
            currWeight += i
            if currWeight > capacity:
                currDays += 1
                currWeight = i
        if currDays > days:
            return 1
        return -1


