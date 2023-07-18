class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        dp = [0] * (maxLength + 1)
        dp[0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, maxLength + 1):
            dp[i] = ((dp[i-zeroGroup] if i >= zeroGroup else 0) + (dp[i-oneGroup] if i >= oneGroup else 0)) % mod
        return sum(dp[i] for i in range(minLength, maxLength + 1)) % mod