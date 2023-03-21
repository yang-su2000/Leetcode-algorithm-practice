class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        for i in nums:
            if not i:
                cur += 1
            else:
                ans += (cur + 1) * cur // 2
                cur = 0
        return ans + (cur + 1) * cur // 2