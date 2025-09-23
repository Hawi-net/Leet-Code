class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
        # Case 1: Single digit
            single_digit = int(s[i-1:i])
            if 1 <= single_digit <= 9:
                dp[i] += dp[i-1]

        # Case 2: Two digits
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]