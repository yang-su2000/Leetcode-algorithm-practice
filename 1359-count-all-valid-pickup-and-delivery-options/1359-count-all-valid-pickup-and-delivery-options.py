class Solution:
    def countOrders(self, n: int) -> int:
        mod = int(1e9) + 7
        ans = 1
        for i in range(1, 2 * n + 1):
            if i % 2 == 0:
                i //= 2
            ans = (ans * i) % mod
        return ans