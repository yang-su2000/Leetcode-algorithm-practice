class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            ib = 1 << i
            ab, bb, cb = a & ib, b & ib, c & ib
            if ab | bb == cb:
                continue
            if ab & bb:
                ans += 2
            else:
                ans += 1
        return ans