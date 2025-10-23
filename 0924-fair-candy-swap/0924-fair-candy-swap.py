class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """
        We leverage hashing and the 
        following relationship:

        sumA - a + b = sumB - b + a ->
        (sumA - sumB) = 2(a - b) -> 
        (sumA - sumB) // 2 = (a - b)
        """
   
        sum_A, sum_B = sum(aliceSizes), sum(bobSizes) 
        bob_set = set(bobSizes)

        delta = (sum_A - sum_B) // 2
        for a in aliceSizes:
            b = a - delta
            if b in bob_set:
                return [a, b]

        return []

        # O(n + m) time. Note: m is len(bobSizes)
        # O(m) space.