class Solution:
    def eraseOverlapIntervals(self, ls: List[List[int]]) -> int:
        ls.sort()
        ans = 0
        end = ls[0][1]
        for i in range(1, len(ls)):
            if ls[i][0] < end:
                ans += 1
                end = min(end, ls[i][1])
            else:
                end = ls[i][1]
        return ans