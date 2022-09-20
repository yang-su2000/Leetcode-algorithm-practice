class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax = cmin = ans = nums[0]
        for i in nums[1:]:
            t = i, i * cmax, i * cmin
            cmax, cmin = max(t), min(t)
            ans = max(ans, cmax)
        return ans