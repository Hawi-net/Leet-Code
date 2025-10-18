class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        count_open = 0
        res = 0
        i = 0
        while i < n:
            if s[i] == '(':
                count_open += 1
                i += 1
                continue
            if i == n - 1 or s[i + 1] != ')':
                res += 1
                i += 1
            else:
                i += 2
            if count_open > 0:
                count_open -= 1
            else:
                res += 1
        # Need to add double ')' for remain opens
        return res + count_open * 2