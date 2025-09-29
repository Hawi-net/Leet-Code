class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num=max(nums)
        max_index=nums.index(max_num)
        for i in range(len(nums)):
            if i!=max_index and max_num<nums[i]*2:
                return -1
        return max_index
        
        