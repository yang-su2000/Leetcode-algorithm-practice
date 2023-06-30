class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        ans = 0
        l, r = 0, n - 1
        lmax, rmax = 0, 0
        while l < r:
            if h[l] < h[r]:
                if lmax < h[l]:
                    lmax = h[l]
                else:
                    ans += lmax - h[l]
                l += 1
            else:
                if rmax < h[r]:
                    rmax = h[r]
                else:
                    ans += rmax - h[r]
                r -= 1
        return ans