from typing import List

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        
        pw = 911382629
        mod = 10**18 + 3
        
        pws = [1] * (n + 1)
        for i in range(1, n + 1):
            pws[i] = (pws[i - 1] * pw) % mod
        
        vis = set()
        for w in words:
            if len(w) > n:
                w = w[:n]
            current_hash = 0
            for c in w:
                current_hash = (current_hash * pw + ord(c)) % mod
                vis.add(current_hash)
        
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = (acc[i] * pw + ord(target[i])) % mod
        
        # Greedy Interval Covering
        cnt = 0
        l = 0
        r = 0
        while r < n:
            nr = r
            for i in range(l, r + 1):
                left = i
                right = n - 1
                best = i
                while left <= right:
                    mid = (left + right) // 2
                    current_hash = (acc[mid + 1] - acc[i] * pws[mid + 1 - i]) % mod
                    if current_hash in vis:
                        best = mid + 1
                        left = mid + 1
                    else:
                        right = mid - 1
                if best > nr:
                    nr = best
            if nr == r:
                return -1
            cnt += 1
            l = r + 1
            r = nr
        return cnt
