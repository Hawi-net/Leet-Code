class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        n = len(nums)
        for i in range(0, n, 2):
            # finding odd number in even index
            if nums[i]%2 == 1:
                # finding replacement even number in odd index
                while nums[j]%2 == 1:j+=2
                # swap
                nums[i], nums[j] = nums[j], nums[i]
        return nums