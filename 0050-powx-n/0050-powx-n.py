class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans