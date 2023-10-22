class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = minval = nums[k]
        l = r = k
        n = len(nums)
        while 0 <= l and r < n:
            while 0 < l and minval <= nums[l-1]:
                l -= 1
            while r < n - 1 and minval <= nums[r+1]:
                r += 1
            ans = max(ans, minval * (r - l + 1))
            if l == 0 and r == n - 1:
                break
            elif l == 0:
                r += 1
                minval = nums[r]
            elif r == n - 1:
                l -= 1
                minval = nums[l]
            elif nums[l-1] > nums[r+1]:
                l -= 1
                minval = nums[l]
            else:
                r += 1
                minval = nums[r]
        return ans