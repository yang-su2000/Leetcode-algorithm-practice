class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
        
    # def __str__(self):
    #     return str(self.val) + '[' + str(self.l) + ', ' + str(self.r) + ']'

class Solution:
    # def __init__(self):
    #     self.dp = [[1] * 1001 for _ in range(1001)]
    #     for j in range(1, 1001):
    #         self.dp[1][j] = j+1
    #         self.dp[j][1] = j+1
    #     for i in range(2, 1001):
    #         for j in range(2, 1001):
    #             self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1]
    
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
        for i in range(1, n):
            val = nums[i]
            node = root
            while node:
                if val < node.val:
                    if node.l:
                        node = node.l
                    else:
                        node.l = Node(val)
                        break
                else:
                    if node.r:
                        node = node.r
                    else:
                        node.r = Node(val)
                        break
        # print(root)
        
        def trace(node):
            nonlocal mod, dp
            if not node:
                return 0, 1
            count1, ans1 = trace(node.l)
            count2, ans2 = trace(node.r)
            return count1 + count2 + 1, (dp[count1][count2] * ans1 * ans2) % mod
        
        count, ans = trace(root)
        # print(count, ans)
        return (ans - 1) % mod