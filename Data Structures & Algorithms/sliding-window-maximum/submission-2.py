class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        ans = []
        m = max(nums[l:k])
        while r < len(nums)+1:
            ans.append(max(nums[l:r]))
            l += 1
            r += 1
        return ans