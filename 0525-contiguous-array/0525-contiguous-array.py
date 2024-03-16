class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        ans = 0
        cur = 0
        for idx, val in enumerate(nums):
            cur += (1 if val else -1)
            if cur in d:
                ans = max(ans, idx - d[cur])
            else:
                d[cur] = idx
        return ans