# brute force
'''
Time complexity: O((m+n)log(m+n)) due to sorting
Space complexity: O(m+n) for the merged array
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2
        else:
            return merged[n//2]
        

# better approach
'''
Time complexity: O(m+n)
Space complexity: O(m+n)

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2
        else:
            return merged[n//2]