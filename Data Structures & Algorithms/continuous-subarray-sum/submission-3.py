class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        yo = {0: -1}
        total = 0   
        for i, n in enumerate(nums):
            total += n
            remainder = total % k
            if remainder in yo and i - yo[remainder] > 1:
                return True
            elif remainder not in yo:
                yo[remainder] = i
        return False