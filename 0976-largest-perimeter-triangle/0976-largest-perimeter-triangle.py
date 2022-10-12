class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        i, j, k = n - 3, n - 2, n - 1
        while 0 <= i < j < k < n:
            if nums[i] + nums[j] > nums[k]:
                return nums[i] + nums[j] + nums[k]
            else:
                k -= 1
                j -= 1
                i -= 1
        return ans
                