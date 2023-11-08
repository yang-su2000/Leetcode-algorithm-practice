class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], s: List[int], nuts: List[List[int]]) -> int:
        ans = 0
        min_dist = inf
        def d(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
        for nut in nuts:
            min_dist = min(min_dist, d(s, nut) - d(tree, nut))
            ans += 2 * d(tree, nut)
        return ans + min_dist