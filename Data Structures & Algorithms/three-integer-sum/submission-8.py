class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        for i, num in enumerate(nums):
            target = -num
            yo = set()
            for j, num2 in enumerate(nums):
                if j == i:
                    continue
                if target-num2 in yo:
                    thing = [num, num2, target-num2]
                    thing.sort()
                    if tuple(thing) not in seen:
                        ans.append(thing)
                        seen.add(tuple(thing))
                        
                yo.add(num2)
        return ans


        
                    
                
