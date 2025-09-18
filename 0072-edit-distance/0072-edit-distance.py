class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dp(i: int, j: int) -> int:

            if i == len(word1):
                insert = len(word2) - j
                return insert

            if j == len(word2):
                delete = len(word1) - i
                return delete
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)

            else:
                insert = 1 + dp(i, j + 1)
                delete = 1 + dp(i + 1, j)
                replace = 1 + dp(i + 1, j + 1)
                return min(delete, replace, insert)

        return dp(0, 0)