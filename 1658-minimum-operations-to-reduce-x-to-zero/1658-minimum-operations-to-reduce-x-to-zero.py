class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = n + 1
        l = 0
        csum = sum(nums)
        for r in range(n):
            csum -= nums[r]
            while csum < x and l <= r:
                csum += nums[l]
                l += 1
            if csum == x:
                ans = min(ans, l + (n - r - 1))
        return ans if ans < n + 1 else -1