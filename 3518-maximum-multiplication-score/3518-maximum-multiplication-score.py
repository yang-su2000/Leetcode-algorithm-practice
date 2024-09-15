class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        best1 = best2 = best3 = best4 = float('-inf')
        for num in b:
            best4 = max(best4, best3 + a[3] * num)
            best3 = max(best3, best2 + a[2] * num)
            best2 = max(best2, best1 + a[1] * num)
            best1 = max(best1, a[0] * num)
        return best4