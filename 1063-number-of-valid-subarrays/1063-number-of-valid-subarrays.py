class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        s = []
        ans = 0
        for i, val in enumerate(nums):
            while s and nums[s[-1]] > val:
                ans += i - s[-1]
                s.pop()
            s.append(i)
        for i in s:
            ans += n - i
        return ans