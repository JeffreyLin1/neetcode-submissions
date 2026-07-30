class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        candidate = nums[0]
        for i in nums:
            if count == 0:
                candidate = i
            elif candidate == i:
                count += 1
            else:
                count -= 1
        return candidate
            
