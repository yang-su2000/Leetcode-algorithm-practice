class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        ans = 0
        i, j = 0, 0
        while j < len(s):
            d[s[j]] += 1
            while len(d) > 2:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans