class Solution:
    def eraseOverlapIntervals(self, ls: List[List[int]]) -> int:
        ls.sort(key=lambda x: x[1])
        cend = ls[0][1]
        ans = 0
        n = len(ls)
        for i in range(1, n):
            start, end = ls[i]
            if cend > start:
                ans += 1
            else:
                cend = end
        return ans