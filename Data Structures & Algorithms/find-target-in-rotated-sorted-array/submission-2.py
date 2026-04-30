class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m
            else:
                print(nums[m])
                break
        
        l, r = 0, len(nums) - 1
        if nums[m] <= target <= nums[r]:
            l = m
        else:
            r = m
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        


        return -1