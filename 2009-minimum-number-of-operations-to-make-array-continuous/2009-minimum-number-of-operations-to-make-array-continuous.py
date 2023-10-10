class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = n
        j = 0
        for i in range(len(nums)):
            r = nums[i] + n - 1
            while j < len(nums) and nums[j] < r:
                j += 1
            if j == len(nums) or nums[j] > r:
                j -= 1
            val = j - i + 1
            ans = min(ans, n - val)
        return ans