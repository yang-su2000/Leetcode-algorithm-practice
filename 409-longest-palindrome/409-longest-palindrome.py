class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        ans = 0
        for i in Counter(s).values():
            if i % 2:
                odd = True
                i -= 1
            ans += i
        return ans + (1 if odd else 0)