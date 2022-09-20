class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        d = [-1] * 128
        d[ord(s[0])] = 0
        l, r = 0, 1
        ans = 1
        while r < n:
            i = ord(s[r])
            if d[i] >= 0:
                while l < d[i] + 1:
                    d[ord(s[l])] = -1
                    l += 1
            d[i] = r
            ans = max(ans, r - l + 1)
            r += 1
            # print(d[ord('a'):])
        return ans