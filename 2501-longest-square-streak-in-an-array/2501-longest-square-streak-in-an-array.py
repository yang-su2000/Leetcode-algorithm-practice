class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        limit = int(1e5)
        for i in s:
            count = 0
            while i <= limit:
                if i in s:
                    count += 1
                    i *= i
                else:
                    break
            ans = max(ans, count)
        return ans if ans > 1 else -1