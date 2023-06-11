class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        ls = [] # (index, val)
        ans = 0
        for i in range(n-1, -1, -1):
            val = 0
            while ls and nums[i] > nums[ls[-1][0]]:
                val = max(val + 1, ls[-1][1])
                ls.pop()
            ls.append((i, val))
            ans = max(ans, val)
        return ans
            