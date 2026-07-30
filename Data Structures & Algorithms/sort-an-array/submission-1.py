class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums) -> List[int]:
            if len(nums) == 1:
                return nums
            
            nums1 = mergeSort(nums[:len(nums)//2])
            nums2 = mergeSort(nums[len(nums)//2:])
            nums3 = []
            l = r = 0
            
            while l < len(nums1) and r < len(nums2):
                print(type(nums1[l]))
                print(type(nums2[r]))
                if nums1[l] > nums2[r]:
                    nums3.append(nums2[r])
                    r += 1
                else:
                    nums3.append(nums1[l])
                    l += 1
            if l < len(nums1):
                nums3 += (nums1[l:])
            elif r < len(nums2):
                nums3 += (nums2[r:])
            return nums3
        return mergeSort(nums)
            