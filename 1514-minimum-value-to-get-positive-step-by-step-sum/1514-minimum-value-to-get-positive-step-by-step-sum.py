class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningSum = 0 #assigning running sum to zero
        minSum = 0 # assigning minimum sum to zero
        for num in nums: # for every num in nums
            runningSum += num # adding current num to runningSum
            minSum = min(minSum, runningSum) # calculating minimum and assigning it to be minSum
        return -minSum + 1 if minSum < 1 else 1 #if minsum is negative, we flip it and add 1 to it else we return 1
        