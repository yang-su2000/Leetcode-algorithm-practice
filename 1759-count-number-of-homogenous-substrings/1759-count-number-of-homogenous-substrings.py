class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        count = 0
        cc = '/'
        for c in s:
            if cc == c:
                count += 1
            else:
                count = 1
                cc = c
            ans += count
        return ans % int(1e9+7)