class Solution:
    def longestPalindrome(self, s: str) -> int:
        uppers = [0] * 26
        lowers = [0] * 26
        for c in s:
            if c >= 'a':
                lowers[ord(c) - ord('a')] += 1
            else:
                uppers[ord(c) - ord('A')] += 1
        odd = False
        ans = 0
        for i in uppers:
            if i % 2:
                odd = True
                i -= 1
            ans += i
        for i in lowers:
            if i % 2:
                odd = True
                i -= 1
            ans += i
        return ans + (1 if odd else 0)