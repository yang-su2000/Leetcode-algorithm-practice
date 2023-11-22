class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        d = defaultdict(int)
        for array in arrays:
            d[max(array)] += 1
        ls = sorted(d.items())[-2:]
        top1, top1c = ls[-1]
        ans = 0
        for array in arrays:
            lo, hi = min(array), max(array)
            if hi != top1 or (hi == top1 and top1c > 1):
                ans = max(ans, top1 - lo)
            elif len(ls) > 1:
                ans = max(ans, ls[-2][0] - lo)
        return ans