from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        r = SortedList(nums[x:])
        ans = inf
        for i in range(n):
            if not r:
                break
            idx = r.bisect_left(nums[i])
            if idx > 0:
                ans = min(ans, abs(r[idx - 1] - nums[i]))
            if idx < len(r):
                ans = min(ans, abs(r[idx] - nums[i]))
            r.pop(r.index(nums[i+x]))
        return ans