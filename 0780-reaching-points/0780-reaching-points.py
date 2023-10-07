class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and (ty - sy) % tx == 0:
                return True
            if ty == sy and (tx - sx) % ty == 0:
                return True
            if tx >= ty:
                tx %= ty
            else:
                ty %= tx
            # print(tx, ty)
        return False