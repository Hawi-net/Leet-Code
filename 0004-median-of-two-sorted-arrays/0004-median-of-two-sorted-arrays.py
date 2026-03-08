class Solution:
    def findMedianSortedArrays(self, nums1: List[int], 
                                     nums2: List[int]) -> float:
        
        n = len(nums1) + len(nums2)

        nums1.append(inf)                                   # <-- 1)
        nums2.append(inf)

        nums1, nums2 = iter(nums1), iter(nums2)             # <-- 2)
        nxt1, nxt2 = next(nums1), next(nums2)
    
        for _ in range((n + 1) //2):
            
            if nxt1 <= nxt2:                                # <-- 3)
                cur, nxt1  = nxt1, next(nums1)
            else: 
                cur, nxt2  = nxt2, next(nums2)

        return cur if n%2 else (cur + min(nxt1, nxt2)) / 2  # <-- 4)
