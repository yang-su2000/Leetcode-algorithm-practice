class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = 'aeiou'
        cur = 0
        for i in range(k):
            if s[i] in v:
                cur += 1
        ans = cur
        for i in range(k, len(s)):
            if s[i-k] in v:
                cur -= 1
            if s[i] in v:
                cur += 1
            ans = max(ans, cur)
        return ans