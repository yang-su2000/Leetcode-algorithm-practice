class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        ls = [0] * 12
        for a, b, val in transactions:
            ls[a] -= val
            ls[b] += val
        ls = [i for i in ls if i]
        ans = inf
        
        def bt(i, val):
            nonlocal ans, ls
            while i < len(ls) and not ls[i]:
                i += 1
            if i == len(ls):
                ans = min(ans, val)
                return
            if val >= ans:
                return
            tmp = ls[i]
            for nxt in range(i + 1, len(ls)):
                ls[nxt] += tmp
                bt(i + 1, val + 1)
                ls[nxt] -= tmp
        
        bt(0, 0)
        return ans
