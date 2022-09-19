class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ls = [10**4+1] * (amount + 1)
        ls[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i-coin >= 0:
                    ls[i] = min(ls[i], ls[i-coin] + 1)
        return -1 if ls[-1] == 10**4+1 else ls[-1]