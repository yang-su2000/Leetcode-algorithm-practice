class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        add = True
        ans = 0
        for b in range(31, -1, -1):
            if (n >> b) & 1:
                if add:
                    ans += (1 << (b + 1)) - 1
                else:
                    ans -= (1 << (b + 1)) - 1
                add = not add
        return ans