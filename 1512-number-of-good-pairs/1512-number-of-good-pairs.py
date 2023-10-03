class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for i in nums:
            ans += d[i]
            d[i] += 1
        return ans