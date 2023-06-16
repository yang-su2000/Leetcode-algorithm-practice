class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
        
    # def __str__(self):
    #     return str(self.val) + '[' + str(self.l) + ', ' + str(self.r) + ']'

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        root = Node(nums[0])
        n = len(nums)
        dp = [[1] * (n+1) for _ in range(n+1)]
        mod = 10**9+7
        for j in range(1, n+1):
            dp[1][j] = j+1
            dp[j][1] = j+1
        for i in range(2, n+1):
            for j in range(2, n+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
        
        def trace(ls):
            nonlocal mod, dp
            if not ls:
                return 1
            l = [i for i in ls if i < ls[0]]
            r = [i for i in ls if i > ls[0]]
            return (dp[len(l)][len(r)] * trace(l) * trace(r)) % mod
        
        ans = trace(nums)
        return (ans - 1) % mod