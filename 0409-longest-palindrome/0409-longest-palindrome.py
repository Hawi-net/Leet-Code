class Solution:
    def longestPalindrome(self, s: str) -> int:
 
        c = Counter(s).values()

        pairCounts = 2 * sum(x>>1 for x in c)

        return pairCounts + (pairCounts < len(s))