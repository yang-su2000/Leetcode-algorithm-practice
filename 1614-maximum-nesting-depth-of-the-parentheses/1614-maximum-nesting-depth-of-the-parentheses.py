class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cur = 0
        for c in s:
            if c == '(':
                cur += 1
            elif c == ')':
                cur -= 1
            ans = max(ans, cur)
        return ans