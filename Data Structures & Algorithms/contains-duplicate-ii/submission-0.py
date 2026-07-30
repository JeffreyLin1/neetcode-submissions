class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes = set()
        l = r = 0
        while r < len(nums):
            if r > k:
                dupes.remove(nums[l])
                l += 1
            dupes.add(nums[r])
            r += 1 
            if len(dupes) != r-l:
                return True
           
        return False 

