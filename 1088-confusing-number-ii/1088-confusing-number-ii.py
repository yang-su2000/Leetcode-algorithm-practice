class Solution:
    def confusingNumberII(self, n: int) -> int:
        m = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        ans = 0
        
        def bt(a, b, mult):
            nonlocal m, ans
            if a > n:
                return
            if a != b:
                # print(a, b, mult)
                ans += 1
            for k, v in m.items():
                bt(a * 10 + k, v * mult + b, mult * 10)
        
        for k, v in m.items():
            if k == 0:
                continue
            bt(k, v, 10)
                
        return ans