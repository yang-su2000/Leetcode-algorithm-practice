class Solution:
    def maxSatisfaction(self, ls: List[int]) -> int:
        ans = 0
        csum = 0
        ctotal = 0
        for i in sorted(ls, reverse=True):
            csum += i
            ctotal += csum
            ans = max(ans, ctotal)
        return ans