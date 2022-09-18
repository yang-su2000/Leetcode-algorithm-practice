class Solution:
    def trap(self, ls: List[int]) -> int:
        n = len(ls)
        ans = 0
        h = 0
        val = 0
        for i in range(n):
            if ls[i] >= h:
                ans += val
                h = ls[i]
                val = 0
            else:
                val += h - ls[i]
        h = 0
        val = 0
        for i in range(n-1, -1, -1):
            if ls[i] > h:
                ans += val
                h = ls[i]
                val = 0
            else:
                val += h - ls[i]
        return ans
            