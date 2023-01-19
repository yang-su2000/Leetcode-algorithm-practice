class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        sum = 0
        ans = 0
        for i in nums:
            sum = (sum + i) % k
            ans += d[sum]
            d[sum] += 1
        return ans
            