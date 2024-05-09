class Solution:
    def maximumHappinessSum(self, ls: List[int], k: int) -> int:
        ls.sort()
        ans = 0
        for i in range(k):
            ans += max(0, ls.pop() - i)
        return ans