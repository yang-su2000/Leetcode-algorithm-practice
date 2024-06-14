class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = [0] * int(2e5 + 2)
        for i in nums:
            count[i] += 1
        ans = 0
        for i in range(int(2e5 + 1)):
            if count[i] > 1:
                ans += count[i] - 1
                count[i + 1] += count[i] - 1
        return ans