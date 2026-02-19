class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s =[]
        for i in range(0,len(nums1)):
            for num in nums1:
                if num in nums2 and num not in s:
                    s.append(num)
        return s
        