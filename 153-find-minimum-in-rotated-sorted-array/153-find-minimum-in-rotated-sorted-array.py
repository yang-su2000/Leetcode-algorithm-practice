class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]