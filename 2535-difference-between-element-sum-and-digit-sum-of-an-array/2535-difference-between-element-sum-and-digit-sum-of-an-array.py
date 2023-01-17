class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        dsum = 0
        for i in nums:
            dsum += sum([int(c) for c in str(i)])
        return abs(sum(nums) - dsum)