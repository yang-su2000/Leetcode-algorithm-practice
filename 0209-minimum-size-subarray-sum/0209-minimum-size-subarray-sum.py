class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0
        i = 0
        n = len(nums)
        while i < n and cur < target:
            cur += nums[i]
            i += 1
        if cur < target:
            return 0
        i -= 1
        l = 0
        r = i
        while cur - nums[l] >= target:
            cur -= nums[l]
            l += 1
        ans = r - l + 1
        # print(l, r)
        r += 1
        while r < n:
            cur += nums[r]
            while cur - nums[l] >= target:
                cur -= nums[l]
                l += 1
            ans = min(ans, r - l + 1)
            r += 1
        return ans