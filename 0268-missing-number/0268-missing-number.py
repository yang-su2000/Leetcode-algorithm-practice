class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        has0 = False
        n = len(nums)
        for i in range(n):
            j = abs(nums[i]) - 1
            if j < 0:
                has0 = True
            else:
                nums[j] *= -1
        if not has0:
            return 0
        idx0 = -1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
            elif nums[i] == 0:
                idx0 = i + 1
        return idx0