class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf
        
        def bt(i, ls, mval, zero_count):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, mval)
                return
            if len(cookies) - i < zero_count:
                return
            if mval >= ans:
                return
            for j in range(k):
                zero_count2 = zero_count - (ls[j] == 0)
                ls[j] += cookies[i]
                bt(i + 1, ls, max(mval, ls[j]), zero_count2)
                ls[j] -= cookies[i]
        
        bt(0, [0] * k, 0, k)
        return ans