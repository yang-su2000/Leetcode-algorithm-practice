class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] # (w, increasing h)
        heights.append(0)
        ans = 0
        for h in heights:
            w = 0
            while s and s[-1][1] >= h:
                pw, ph = s.pop()
                ans = max(ans, (w + pw) * ph)
                w += pw
            s.append((w + 1, h))
            # print(s[-1], end=' ')
        # print()
        return ans