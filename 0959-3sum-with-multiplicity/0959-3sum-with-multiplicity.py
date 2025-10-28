from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        result = 0
        
        for i in count:
            for j in count:
                k = target - i - j
                if k in count:
                    if i == j == k:
                        result += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                    elif i == j != k:
                        result += count[i] * (count[i] - 1) // 2 * count[k]
                    elif i < j < k:
                        result += count[i] * count[j] * count[k]
        
        return result % MOD