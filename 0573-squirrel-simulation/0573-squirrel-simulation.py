class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], s: List[int], nuts: List[List[int]]) -> int:
        def d(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
        ans = sum(d(tree, nut) for nut in nuts)
        min_dist = min(d(s, nut) - d(tree, nut) for nut in nuts)
        return 2 * ans + min_dist