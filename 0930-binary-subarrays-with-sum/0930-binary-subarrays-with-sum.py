class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        cur = 0
        for i in nums:
            cur += i
            ans += d[cur - goal]
            d[cur] += 1
        return ans