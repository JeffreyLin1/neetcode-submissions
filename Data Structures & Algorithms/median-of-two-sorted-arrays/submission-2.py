class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, len(nums1)
        half = (len(nums1) + len(nums2))//2
        while l < r:
            mid = (l + r) // 2
            mid2 = half - mid
            if mid2 > 0 and mid < len(nums1) and nums2[mid2 - 1] > nums1[mid]:
                l = mid + 1   
            else:
                r = mid
        mid = l
        mid2 = half - mid
        nums1_left = nums1[mid - 1] if mid > 0 else float("-inf")
        nums1_right = nums1[mid] if mid < len(nums1) else float("inf")
        nums2_left = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
        nums2_right = nums2[mid2] if mid2 < len(nums2) else float("inf") 

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
        return min(nums1_right, nums2_right)

        '''
        1. create random potential partition for nums1 (numbers from the array that will be on 
        left side of combined array)
            - let this partition be 'mid'
        2. compute the equivalent partition for nums2, which is half - nums1partition
            - let this partition be 'mid2'
        3. check if its valid
            - if nums1[mid - 1] > nums2[mid]
                - partition needs to be smaller
            - if nums2[mid - 1] > nums1[mid] 
                - partition needs to be larger
        '''
