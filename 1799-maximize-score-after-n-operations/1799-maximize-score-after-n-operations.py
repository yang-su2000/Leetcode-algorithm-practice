from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        nn = (1 << n)
        dp = [-1] * nn
        
        def bt(ls, mask, count):
            nonlocal n, nn, dp
            if 2 * count == n:
                return 0
            if dp[mask] != -1:
                return dp[mask]
            ans = 0
            for i in range(len(ls)):
                for j in range(i+1, len(ls)):
                    if ((1 << i) & mask) or ((1 << j) & mask):
                        continue
                    mask2 = mask | (1 << i) | (1 << j)
                    cur = (count + 1) * gcd(ls[i], ls[j]) + bt(ls, mask2, count+1)
                    ans = max(ans, cur)
            dp[mask] = ans
            return ans
        
        return bt(nums, 0, 0)