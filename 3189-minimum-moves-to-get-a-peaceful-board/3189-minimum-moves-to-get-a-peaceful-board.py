class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        ans = 0
        rows = [r for r, _ in rooks]
        cols = [c for _, c in rooks]
        for idx, r in enumerate(sorted(rows)):
            ans += abs(r - idx)
        for idx, c in enumerate(sorted(cols)):
            ans += abs(c - idx)
        return ans