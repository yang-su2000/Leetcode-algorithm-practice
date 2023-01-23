class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert_map = {0: 0, 1: 1, 8: 8, 6: 9, 9: 6}
        ans = 0
        n_ = n
        while n:
            cur = n % 10
            if cur not in invert_map:
                return False
            ans = ans * 10 + invert_map[cur]
            n //= 10
        return ans != n_
            