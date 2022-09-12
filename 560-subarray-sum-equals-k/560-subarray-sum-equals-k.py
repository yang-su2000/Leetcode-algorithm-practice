class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        sum = 0
        d[sum] += 1
        for num in nums:
            sum += num
            # want to find ? = k, cur - ? = prev, so find cur - k = prev
            ans += d[sum - k]
            d[sum] += 1
        return ans