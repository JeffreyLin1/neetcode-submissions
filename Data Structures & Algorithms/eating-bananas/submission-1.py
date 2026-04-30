class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k: 1 -> max(piles)
        # using binary search:
        # k = 50
        # iterate through entire array to determine hours spent eating
        # hours > h, that means we have to eat more bananas -> l = m+1
        # hours < h, other way around

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            m = (l + r) // 2
            ho = 0
            for i in piles:
                ho += math.ceil(i/m)
            if ho > h:
                l = m + 1
            elif ho <= h:
                r = m - 1
                ans = min(ans, m)
        return ans



            


    
