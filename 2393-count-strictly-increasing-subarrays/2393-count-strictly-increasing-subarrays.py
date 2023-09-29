class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            ans += count
        return ans