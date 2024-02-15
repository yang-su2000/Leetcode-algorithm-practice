class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        csum = sum(nums[:2])
        ans = -1
        for i in range(2, n):
            if nums[i] < csum:
                ans = max(ans, csum + nums[i])
            csum += nums[i]
        return ans