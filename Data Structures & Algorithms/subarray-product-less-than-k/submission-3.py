class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        curr = 1
        for r in range(len(nums)):
            curr *= nums[r]
            while l <= r and curr >= k:
                curr //= nums[l]
                l += 1
            ans += r- l + 1

        return ans

            

            
