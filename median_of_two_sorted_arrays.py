class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                result.append(nums1[0])
                nums1.pop(0)
            else: 
                result.append(nums2[0])
                nums2.pop(0)
        
        result = result + nums1 + nums2
        
        if len(result) % 2 == 0:
            mid1 = int(len(result) / 2)
            mid2 = mid1 - 1
            return (result[mid1] + result[mid2]) / 2
        else:
            mid = int(len(result) / 2)
            return (result[mid])