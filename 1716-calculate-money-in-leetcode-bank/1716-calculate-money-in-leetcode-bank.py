class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        start = 1
        while n >= 7:
            ans += (start + 3) * 7
            start += 1
            n -= 7
        return ans + (start + start + n - 1) * n // 2