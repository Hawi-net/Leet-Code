class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]
        return[]
def twosum(num,target):
    notebook = {}
    for i in range(len(num)):
        current_num = num[i]
        neded_num = target - current_num
        if neded_num in notebook:
            return [notebook[neded_num],i]
        notebook[current_num] = i
    return
print(twosum([1,2,3,4,5],9))
        