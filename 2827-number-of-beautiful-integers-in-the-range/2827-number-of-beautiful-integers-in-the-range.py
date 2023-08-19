class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def get(val):
            # 30, 20, 30, 2, 2 * 10 = 7.2e5
            @cache
            def dp(even, mod, idx, bounded, leading_zero):
                if abs(even) > 15:
                    return 0
                if idx == len(val):
                    return (even == 0 and mod == 0)
                ret = 0
                if leading_zero:
                    ret += dp(even, mod, idx + 1, False, True)
                l = 1 if leading_zero else 0
                r = int(val[idx]) if bounded else 9
                for i in range(l, r + 1):
                    even2 = even
                    if i % 2 == 0:
                        even2 += 1
                    else:
                        even2 -= 1
                    mod2 = (mod * 10 + i) % k
                    ret += dp(even2, mod2, idx + 1, bounded and i == r, False)
                return ret
            return dp(0, 0, 0, True, True)
        
        hi = get(str(high))
        lo = get(str(low - 1))
        # print(hi, lo)
        return hi - lo