class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        ans = 0
        for sign in ['T', 'F']:
            l = 0
            op = k
            for r in range(len(s)):
                if s[r] != sign:
                    op -= 1
                    while op < 0:
                        if s[l] != sign:
                            op += 1
                        l += 1
                ans = max(ans, r - l + 1)
        return ans
                    