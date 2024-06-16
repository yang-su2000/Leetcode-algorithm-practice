class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        cur = 0
        i = 0
        while cur < n and i < len(nums):
            if cur + 1 < nums[i]:
                cur += cur + 1
                ans += 1
            else:
                cur += nums[i]
                i += 1
        while cur < n:
            cur += cur + 1
            ans += 1
        return ans