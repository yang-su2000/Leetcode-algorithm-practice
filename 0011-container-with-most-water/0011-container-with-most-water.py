class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            ans = max(ans, min(h[l], h[r]) * (r - l))
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans