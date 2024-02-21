class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for b in range(31, -1, -1):
            x, y = left & (1 << b), right & (1 << b)
            if x & y:
                ans |= (1 << b)
            elif x ^ y:
                break
        return ans
                