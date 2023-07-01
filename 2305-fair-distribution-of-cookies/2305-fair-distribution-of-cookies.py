class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf
        
        def bt(i, ls, mval):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, mval)
                return
            if mval >= ans:
                return
            for j in range(k):
                ls[j] += cookies[i]
                bt(i + 1, ls, max(mval, ls[j]))
                ls[j] -= cookies[i]
        
        bt(0, [0] * k, 0)
        return ans