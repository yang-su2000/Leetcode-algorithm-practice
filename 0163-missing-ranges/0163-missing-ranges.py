class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        if nums[0] != lower:
            nums = [lower-1] + nums
        if nums[-1] != upper:
            nums.append(upper+1)
        n = len(nums)
        ans = []
        for i in range(n-1):
            a, b = nums[i], nums[i+1]
            if a < b-1:
                ans.append([a+1, b-1])
        return ans
        