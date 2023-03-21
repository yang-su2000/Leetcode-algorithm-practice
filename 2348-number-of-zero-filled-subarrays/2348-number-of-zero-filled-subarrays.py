class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        for i in nums:
            if not i:
                cur += 1
                ans += cur
            else:
                cur = 0
        return ans