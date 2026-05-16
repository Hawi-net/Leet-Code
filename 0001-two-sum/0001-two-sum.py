class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notebook = {}
        for i in range(len(nums)):
            current_num = nums[i]
            neded_num = target - current_num
            if neded_num in notebook:
                print([notebook[neded_num],i])
                return [notebook[neded_num],i]
            notebook[current_num] = i
        return [-1,-1]
                
                