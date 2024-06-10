class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        for a, b in zip(heights, sorted(heights)):
            ans += (a != b)
        return ans