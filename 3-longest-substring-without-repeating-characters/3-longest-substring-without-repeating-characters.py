class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = [None] * 128
        l, r = 0, 0
        ans = 0
        while r < n:
            i = ord(s[r])
            if d[i] is not None and l <= d[i] < r:
                l = d[i] + 1
            d[i] = r
            ans = max(ans, r - l + 1)
            r += 1
        return ans