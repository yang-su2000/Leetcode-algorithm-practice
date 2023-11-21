class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for i in nums:
            val = i - int(str(i)[::-1])
            ans += d[val]
            d[val] += 1
        return ans % int(1e9+7)