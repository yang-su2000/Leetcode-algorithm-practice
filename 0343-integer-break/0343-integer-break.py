class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        for k in range(2, n + 1):
            cur = 1
            each = n // k
            remain = n % k
            for _ in range(k):
                if remain:
                    remain -= 1
                    cur *= each + 1
                else:
                    cur *= each
            ans = max(ans, cur)
        return ans